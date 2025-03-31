"""
Pipeline to fetch emails from Gmail
"""

from scripts.gmail_client import GmailClient

def gmail_pipeline(): 

    """
    Pipeline to fetch emails from Gmail 
    return: 
        responses_dictionary with ID, Subject, Body of the email
        gmail_client: Gmail client object
    """

    gmail = GmailClient()
    gmail_client = gmail.service
    query = gmail.build_query()
    
    responses_dictionary = gmail.fetch_email_details(gmail_client, query)

    return responses_dictionary, gmail_client
