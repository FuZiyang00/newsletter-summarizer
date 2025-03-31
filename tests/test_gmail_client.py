"""
Unit tests for the GmailClient class.

This module contains test cases for verifying the functionality of the GmailClient
class methods, ensuring correct initialization, query building, email extraction,
and fetching email details.
"""


import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from scripts.gmail_client import GmailClient

class TestGmailClient(unittest.TestCase):

    """
    Test suite for the GmailClient class.

    This class tests various methods of GmailClient to validate its behavior in
    fetching and processing emails.
    """

    @patch("scripts.gmail_client.build") # Mocks build() from the googleapiclient.discovery
    @patch("scripts.gmail_client.Credentials.from_authorized_user_file")
    def test_get_gmail_client(self, mock_credentials, mock_build):
        """
        Test the get_gmail_client method to ensure it initializes the Gmail service correctly.
        Arguments:
            mock_credentials: Mocked credentials object.
            mock_build: Mocked build function from googleapiclient.discovery.
        """
        mock_creds = MagicMock() # Mocks the loading of credentials
        mock_credentials.return_value = mock_creds

        mock_service = MagicMock()
        mock_build.return_value = mock_service
        client = GmailClient()
        self.assertEqual(client.service, mock_service)
        mock_build.assert_called_once_with("gmail", "v1", credentials=mock_creds) # Check if build was called with correct parameters


    def test_build_query(self):
        """
        Test the build_query method to ensure it constructs the correct query string.
        """

        now_date = datetime.now()
        client = GmailClient()

        # Mock the datetime to return a specific date
        expected_time = now_date - timedelta(days=7)
        returned_time = client.get_last_run_time(now_date)
        self.assertEqual(returned_time, expected_time)

        # test the query construction
        query = client.build_query()
        self.assertEqual(query, f"is:unread after:{returned_time.strftime('%Y/%m/%d')}")


    def test_extract_email_body(self):
        """
        Test the extract_email_body method to ensure it correctly extracts the email body.
        """
        email_data = {
            "payload": {
                "parts": [
                    {"mimeType": "text/plain", "body": {"data": "SGVsbG8gd29ybGQ="}}
                ]
            }
        }
        expected_body = "Hello world"
        self.assertEqual(GmailClient.extract_email_body(email_data), expected_body)


    @patch("scripts.gmail_client.GmailClient.extract_email_body") # Mocks extract_email_body method
    def test_fetch_email_details(self, mock_extract_email_body):
        """
        Test the fetch_email_details method to ensure it correctly fetches email details.
        Arguments:
            mock_extract_email_body: Mocked extract_email_body method.
        """
        mock_service = MagicMock() # Generic mock for the Gmail service
        mock_extract_email_body.return_value = "Test Body"

        mock_service.users().messages().list().execute.return_value = {
            "messages": [{"id": "123"}]
        }
        mock_service.users().messages().get().execute.return_value = {
            "payload": {"headers": [{"name": "From", "value": "test@example.com"}]}
        }

        client = GmailClient()
        emails = client.fetch_email_details(mock_service, "is:unread")

        self.assertEqual(len(emails), 1)
        self.assertEqual(emails[0]["sender"], "test@example.com")
        self.assertEqual(emails[0]["body"], "Test Body")

if __name__ == "__main__":
    unittest.main()
