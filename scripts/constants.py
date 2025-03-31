"""
File where all the constants are defined 
"""

CREDENTIALS_FILE = 'credentials.json' # Path to the credentials file for the first time access

TOKEN_FILE = 'token.json' # Path to the token file

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", 
          "https://www.googleapis.com/auth/gmail.modify"] # granted permissions

OPENAI_MODEL = "gpt-4o" # OpenAI model to use

EMAIL_LIMIT = 2

DISPLAY_SPEED = 0.01
