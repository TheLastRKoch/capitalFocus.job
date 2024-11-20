from google.oauth2 import service_account
from googleapiclient.discovery import build


class ServiceGmail:

    def __init__(self, service_account_file, scopes):
        self.credentials = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def get_message_list(self, user_id='me', query=None, max_results=500, label_ids=None):
        try:
            messages = []
            request = self.service.users().messages().list(userId=user_id, q=query,
                                                           maxResults=max_results, labelIds=label_ids)
            response = request.execute()

            if 'messages' in response:
                messages.extend(response['messages'])

            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                request = self.service.users().messages().list(
                    userId=user_id,
                    q=query,
                    pageToken=page_token,
                    maxResults=max_results,
                    labelIds=label_ids)
                response = request.execute()
                if 'messages' in response:
                    messages.extend(response['messages'])

            return messages

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_message(self, user_id, msg_id, format='raw'):
        try:
            message = self.service.users().messages().get(
                userId=user_id, id=msg_id, format=format).execute()
            return message
        except Exception as error:
            print(f'An error occurred: {error}')
            return None
