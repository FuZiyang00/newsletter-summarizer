from scripts.llm import LLM
from scripts.prompts import (
    RESTRUCTURE_INSTRUCTIONS,
    RESTRUCTURE_ROLE,
    RESTRUCTURE_EXAMPLE, 

    SUMMARY_INSTRUCTIONS,
    SUMMARY_ROLE,
    SUMMARY_EXAMPLE
)


def LLM_pipeline(email_content: str) -> str:
    """
    Pipeline to restructure email and summarize its content using the LLM model.
    """
    llm = LLM()
    restructure_prompt, restructure_role = llm.prompt_generator(
        RESTRUCTURE_INSTRUCTIONS,
        email_content,
        RESTRUCTURE_EXAMPLE,
        RESTRUCTURE_ROLE
    )

    restructured_email_content = llm.generate_response(restructure_prompt, restructure_role)

    summary_prompt, summary_role = llm.prompt_generator(
        SUMMARY_INSTRUCTIONS,
        restructured_email_content,
        SUMMARY_EXAMPLE,
        SUMMARY_ROLE
    )

    summary_email_content = llm.generate_response(summary_prompt, summary_role)
    return summary_email_content