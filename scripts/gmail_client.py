from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError 

from .constants import (
    SCOPES, 
    TOKEN_FILE, 
    CREDENTIALS_FILE)

import os
from datetime import datetime, timedelta
import base64
import logging
from typing import List, Dict, Any

class GmailClient:

    def __init__(self):
        self.service = self.get_gmail_client()

    def get_gmail_client(self) -> Resource:
        """Creates and returns a Gmail client."""

        creds = None
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=8080)
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
        return build("gmail", "v1", credentials=creds)
    

    def get_last_run_time(self) -> datetime:
        """Gets the last run time from file or returns a default time."""

        return datetime.now() - timedelta(days=7)  # Default to 7 days ago if no last run
    

    def build_query(self) -> str:
        """Builds the query string for fetching emails."""

        last_run = self.get_last_run_time()
        return f"is:unread after:{last_run.strftime('%Y/%m/%d')}"
    
    @staticmethod
    def extract_email_body(email_data: dict) -> str:
        """Extracts the plain text body from the email data."""
        try:
            parts = email_data.get("payload", {}).get("parts", [])
            for part in parts:
                if part.get("mimeType") == "text/plain":
                    return base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
            return "No plain text body found"
        except Exception as e:
            logging.error(f"Error extracting email body: {e}")
            return "Error reading email body"
    

    def fetch_email_details(self, gmail: Resource, query: str) -> List[Dict[str, Any]]:
        """Fetches email sender and content based on the given query."""
        try:
            # Step 1: Fetch list of emails matching the query
            results = gmail.users().messages().list(userId="me", q=query).execute()
            messages = results.get("messages", [])
            
            emails_data = []

            # Step 2: Fetch details for each email
            for message in messages:
                email_id = message["id"]
                email_data = gmail.users().messages().get(userId="me", id=email_id, format="full").execute()

                # Step 3: Extract sender and content
                headers = email_data.get("payload", {}).get("headers", [])
                sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown Sender")
                body = self.extract_email_body(email_data)

                emails_data.append({"id": email_id, "sender": sender, "body": body})

            return emails_data

        except HttpError as error:
            logging.error(f"Failed to fetch email details: {error}")
            return []
    
    @staticmethod
    def mark_emails_as_read(gmail: Resource, email_id: str) -> None:
        """Marks the given email as read by removing the UNREAD label."""
        try:
            gmail.users().messages().modify(
                userId="me",
                id=email_id,
                body={"removeLabelIds": ["UNREAD"]}
            ).execute()
            print(f"Marked email {email_id} as read.")
        except HttpError as error:
            logging.error(f"Failed to mark email as read: {error}")
