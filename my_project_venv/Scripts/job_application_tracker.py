import os
import base64
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    token_file = 'token.json'

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def fetch_emails():
    service = get_gmail_service()

    # Use the Gmail API to fetch emails
    # You may need to customize the query based on your emails
    results = service.users().messages().list(userId='me', q='subject:"Job Application"').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            process_email(msg)

def process_email(msg):
    # Extract relevant information from the email
    subject = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject'][0]
    body = base64.urlsafe_b64decode(msg['payload']['parts'][0]['body']['data']).decode('utf-8')

    # Customize this part based on your email structure
    if "Interview Invitation" in subject:
        status = "Interview Call"
    elif "Application Rejected" in subject:
        status = "Application Rejected"
    else:
        status = "Other Status"

    # Store the information in an Excel file or any other desired format
    with open('job_applications.csv', 'a') as file:
        file.write(f'{subject},{status},{body}\n')

if __name__ == '__main__':
    fetch_emails()