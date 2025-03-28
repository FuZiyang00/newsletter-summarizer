import os
from openai import OpenAI
import logging
from .constants import OPENAI_MODEL

class LLM:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")  # Use GitHub secret

        if not api_key:
            raise ValueError("API Key is missing! Set OPENAI_API_KEY as an environment variable.")
        
        self.openai = OpenAI(api_key=api_key)

    @staticmethod
    def prompt_generator(instructions: str, email_content: str, example: str, role: str) -> str:
        prompt = f"""
            Instructions:
            {instructions}

            Email content:
            {email_content}

            Example:
            {example}
            """
        
        role = f"""
            {role}
            """
        return prompt, role


    def generate_response(self, prompt: str, role: str) -> str:
        """
        Uses OpenAI's API to clean and structure newsletter emails for better ingestion by an LLM.
        
        Args:
            prompt (str): The instructions to the model + raw email content.
            role (str): The role assigned to the AI in the prompt.
            
        Returns:
            str: The cleaned and structured email content.

        """
    
        try:
            response = self.openai.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": role},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            logging.error(f"Error in OpenAI categorization: {e}")
            return "Other"
