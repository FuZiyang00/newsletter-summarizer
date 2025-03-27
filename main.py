from scripts.constants import EMAIL_LIMIT, DISPLAY_SPEED
from scripts.utils import progressive_print
from scripts.gmail_client import GmailClient
from pipelines.gmail_client_pipeline import Gmail_pipeline
from pipelines.llm_response_pipeline import LLM_pipeline
import multiprocessing

def summarize_email(body, queue): 
    """Function to run LLM_pipeline in a separate process."""
    summarized_content = LLM_pipeline(body)
    queue.put(summarized_content)  # Place the result in the queue


def main(): 
    # Fetching emails from Gmail
    responses_dictionary, gmail_client = Gmail_pipeline()

    for i in range(EMAIL_LIMIT):

        queue = multiprocessing.Queue()
        process = multiprocessing.Process(target=summarize_email, args=(responses_dictionary[i]["body"], queue))
        process.start()

        print(f"Subject: {responses_dictionary[i]['sender']}\n")
        progressive_print("Body: ", responses_dictionary[i]["body"], DISPLAY_SPEED)
        print("\n")

        process.join()  # Wait for the LLM process to finish
        summarized_email_content = queue.get() if not queue.empty() else None

        if summarized_email_content:
            progressive_print("Summarized Email: ", summarized_email_content, DISPLAY_SPEED)
            GmailClient.mark_emails_as_read(gmail_client, responses_dictionary[i]["id"])
            print("\n\n")
        else:
            print("Failed to summarize email. Skipping to next email...\n\n")


if __name__ == "__main__":
    
    main()
