"""
This module provides a class for interacting with OpenAI's API 
to generate responses based on given prompts.
It includes methods for generating prompts and processing responses.
"""
import os
import logging
from openai import OpenAI
from .constants import OPENAI_MODEL

class LLM:
    
    """
    A class to interact with OpenAI's API for generating responses based on prompts.
    """

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")  # Use GitHub secret

        if not api_key:
            raise ValueError("API Key is missing! Set OPENAI_API_KEY as an environment variable.")
        
        self.openai = OpenAI(api_key=api_key)

    @staticmethod
    def prompt_generator(instructions: str, email_content: str, example: str, role: str) -> str:
        """
        Generates a prompt for the OpenAI model by combining the provided instructions, 
        email content, example, and role.
        """
        
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
        
        except Exception as openai_error:
            logging.error("Error in OpenAI categorization: %s", openai_error)
            return "Other"
