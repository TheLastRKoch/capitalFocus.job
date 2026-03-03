from typing import Optional
import base64
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.readonly',
]

# Change this path to where your credentials are
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'


def _find_body_parts(parts):
    html_part = None
    text_part = None

    for part in parts:
        mime = part.get('mimeType')
        body = part.get('body', {})
        if mime == 'text/html' and 'data' in body:
            html_part = body['data']
        elif mime == 'text/plain' and 'data' in body:
            text_part = body['data']
        if 'parts' in part:
            _find_body_parts(part['parts'])


def get_gmail_service():
    creds = None

    # The file token.json stores the user's access and refresh tokens
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid credentials use login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def get_email_list(service, query):
    return service.users().messages().list(userId='me', q=query).execute()


def get_email_html(service,
                   message_id: str,
                   prefer_html: bool = True,
                   fallback_to_text: bool = True) -> Optional[str]:
    try:
        msg = service.users().messages().get(userId='me',
                                             id=message_id,
                                             format='full').execute()
    except HttpError as e:
        print(f"Error fetching message {message_id}: {e}")
        return None

    payload = msg.get('payload', {})

    breakpoint()

    if 'body' in payload and 'data' in payload['body']:
        data = payload['body']['data']
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')

    # Look for parts
    html_part = None
    text_part = None

    if 'parts' in payload:
        _find_body_parts(payload['parts'])

    # Choose content
    if prefer_html and html_part:
        data = html_part
    elif text_part and fallback_to_text:
        data = text_part
        text = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
        return f"<pre style='white-space: pre-wrap; font-family: monospace;'>{text}</pre>"
    elif html_part:
        data = html_part
    else:
        print(f"No body content found in message {message_id}")
        return None

    try:
        html = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
        return html
    except Exception as e:
        print(f"Decode error: {e}")
        return None


def move_to_label(service,
                  message_id: str,
                  label_name: str,
                  create_if_missing: bool = False) -> bool:
    try:
        # Get all labels
        results = service.users().labels().list(userId='me').execute()
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
            created = service.users().labels().create(
                userId='me', body=new_label_body).execute()
            label_id = created['id']
            print(f"Created new label: {label_name}")

        if not label_id:
            print(f"Label '{label_name}' not found and creation not allowed.")
            return False

        # Modify labels
        body = {'addLabelIds': [label_id], 'removeLabelIds': ['INBOX']}

        service.users().messages().modify(userId='me',
                                          id=message_id,
                                          body=body).execute()

        print(f"✓ Moved {message_id} → {label_name}")
        return True

    except HttpError as e:
        print(f"API error while moving {message_id}: {e}")
        return False


if __name__ == '__main__':

    service = get_gmail_service()

    email_list = get_email_list(service, "label:job-new")["messages"]

    for email in email_list:
        html_content = get_email_html(service, email["id"])
        print(html_content)
        breakpoint()

    # 2. Move to label
    # success = move_to_label(service,
    #                        TEST_MESSAGE_ID,
    #                        label_name="Receipts/2025",
    #                        create_if_missing=True)
