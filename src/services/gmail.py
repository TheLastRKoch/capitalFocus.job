from typing import Optional
import base64
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from utils.format import base_64_decode

SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.readonly',
]

CREDENTIALS_FILE = 'src/secrets/credentials.json'
TOKEN_FILE = 'src/secrets/token.json'


class GmailService:

    def __init__(self):
        creds = None

        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)

            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())

        self.engine = build('gmail', 'v1', credentials=creds)

    def _find_body_parts(self, parts):
        html_part = None
        text_part = None

        for part in parts:
            mime = part.get('mimeType')
            body = part.get('body', {})

            if mime == 'text/plain':
                if 'data' in body:
                    text_part = body['data']

            if mime in ['text/html', 'multipart/related']:
                if 'data' in body:
                    html_part = body['data']

            if 'parts' in part:
                child_text, child_html = self._find_body_parts(part['parts'])

                if child_text:
                    text_part = child_text
                if child_html:
                    html_part = child_html

        return text_part, html_part

    def get_email_content(self, email):
        text = None
        html = None

        payload = email.get('payload', {})

        if 'body' in payload and 'data' in payload['body']:
            data = payload['body']['data']
            return base64.urlsafe_b64decode(data).decode('utf-8',
                                                         errors='replace')

        if 'parts' in payload:
            encoded_text, encoded_html = self._find_body_parts(
                payload['parts'])

        if encoded_text:
            text = base_64_decode(encoded_text)

        if encoded_html:
            html = base_64_decode(encoded_html)

        return text, html

    def get_message(self,
                    message_id: str,
                    prefer_html: bool = True,
                    fallback_to_text: bool = True) -> Optional[str]:
        try:
            return self.engine.users().messages().get(userId='me',
                                                      id=message_id,
                                                      format='full').execute()
        except HttpError as e:
            print(f"Error fetching message {message_id}: {e}")
            return None

    def get_email_list(self, query):
        return self.engine.users().messages().list(userId='me',
                                                   q=query).execute()

    def get_label_list(self):
        return self.engine.users().labels().list(userId='me').execute()

    '''
    FIXME: This method add a label but do not remove the previos label
    current_labels = message.get('labelIds', [])
    '''
    def move_to_label(self,
                      message_id: str,
                      label_name: str,
                      create_if_missing: bool = False) -> bool:
        try:
            results = self.engine.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])

            label_id = None
            for lbl in labels:
                if lbl['name'].lower() == label_name.lower():
                    label_id = lbl['id']
                    break

            # Create label if allowed and not found
            if not label_id and create_if_missing:
                new_label_body = {
                    'name': label_name,
                    'labelListVisibility': 'labelShow',
                    'messageListVisibility': 'show'
                }
                created = self.engine.users().labels().create(
                    userId='me', body=new_label_body).execute()
                label_id = created['id']
                print(f"Created new label: {label_name}")

            if not label_id:
                print(
                    f"Label '{label_name}' not found and creation not allowed."
                )
                return False

            body = {'addLabelIds': [label_id], 'removeLabelIds': ['INBOX']}

            self.engine.users().messages().modify(userId='me',
                                                  id=message_id,
                                                  body=body).execute()

            return True

        except HttpError:
            return False
