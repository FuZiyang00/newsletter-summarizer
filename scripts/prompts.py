"""
# Prompt, Role and Example for restructuring the email content
"""

# instruction 
RESTRUCTURE_INSTRUCTIONS = """ 
1. Preserve Essential Metadata

    From: Retain the sender's name and email address.

    Date: Keep the original email timestamp.

    Subject: Ensure the subject line is included.

2. Structure the Email for Readability

    Format the content using clear section headers, bullet points, and concise paragraphs.

    Do not alter the meaning or summarize—just reformat for clarity.

    Use Markdown-style headings where appropriate (e.g., ## Section Title).

    Remove any unnecessary formatting or HTML tags 

    Remove emojis and special characters that do not add value to the content.

3. Remove Non-Content Elements

    Delete interaction links (e.g., "Subscribe," "Sign up," "Click here").

    Remove marketing phrases (e.g., "Act now! Limited time offer!").

    Discard full URLs unless they are essential to understanding the content. Instead, keep only the source name (e.g., Source: Tech Digest).

4. Ensure Consistency & Clarity

    Retain only factual, useful content in a neutral tone.

    Use simple, structured formatting to enhance LLM comprehension
"""

# role
RESTRUCTURE_ROLE = """ 
You are an AI assistant designed to prepare newsletter emails for efficient processing by a large language model (LLM). 
Your goal is to clean, structure, and standardize the content while removing irrelevant elements that do not contribute to the core informational value.
"""

# example
RAW_EMAIL = """
Raw Email Content:
    From: AI Weekly <newsletter@aiweekly.com>
    Date: March 22, 2025
    Subject: The Future of AI

    Hello,

    We're thrilled to bring you the latest AI updates! 🚀  

    **Big Tech's AI Expansion**  
    - OpenAI, Google, and Meta are rolling out AI models faster than ever.  
    - AI-generated content is now in consumer apps.  

    **AI Regulations Incoming**  
    - The EU is working on an AI Act for ethical guidelines.  
    - The US is drafting stricter data privacy laws.  

    Subscribe now for exclusive insights!  

    Read more: [https://aiweekly.com/future-of-ai]  

    Best,  
    AI Weekly Team
"""

PROCESSED_EMAIL = """
Processed Email Content:
    ## The Future of AI  

    ### Big Tech's AI Expansion  
    - OpenAI, Google, and Meta are rolling out AI models rapidly.  
    - AI-generated content is now integrated into consumer applications.  

    ### AI Regulations Incoming  
    - The EU is drafting an AI Act to establish ethical guidelines.  
    - The US is considering stricter data privacy laws related to AI.  

    **Source:** AI Weekly
"""

RESTRUCTURE_EXAMPLE = RAW_EMAIL + PROCESSED_EMAIL 

"""
Prompt, Role and Example for summarizing the email content
"""

# role
SUMMARY_ROLE = """
You are an AI assistant specialized in structuring and summarizing newsletter content for optimal understanding.
The emails content hierarchy is presented with a markdown format. 
Your task is to generate a concise yet comprehensive summary of the provided email, ensuring that key insights are preserved while removing unnecessary details.
The summary should retain the core message, main topics, and any essential context while discarding marketing fluff, promotional language, and redundant explanations.
"""

# instruction
SUMMARY_INSTRUCTIONS = """ 
Below is a cleaned and structured version of a newsletter email that has already been processed to remove unnecessary elements. 
Your task is to generate a structured summary that retains the key points while ensuring brevity and clarity. 
Please follow these guidelines: 

1. Retain essential information: Focus on key insights, main topics, and relevant context.
2. Omit unnecessary details: Ignore promotional content, repetitive statements, and general marketing language.
3. Preserve factual accuracy: Ensure that all summarized points accurately reflect the original message.
4. Format for readability: Structure the summary with bullet points or sections for easy reading.
5. Keep it concise: Aim for a well-structured summary that efficiently captures the key takeaways in a few sentences or bullet points.
"""

# example
COMPLETE_EMAIL = """
Complete Email:
Subject: AI Trends in 2025  

The AI industry is evolving rapidly, with significant advancements in multimodal AI, autonomous agents, and efficiency improvements in model training.  
- Multimodal AI is enhancing interactions by combining text, image, and audio processing.  
- AI-powered agents are becoming more autonomous, streamlining workflows in industries like healthcare and finance.  
- New techniques in model training reduce computational costs, making AI more accessible.  
- Challenges remain in ethical AI development and regulatory compliance.  
"""

EMAIL_SUMMARY = """ 

Desired Summary:
AI Trends in 2025 - Key Takeaways:
- Multimodal AI: Improved integration of text, image, and audio for enhanced interactions.
- Autonomous AI Agents: Increasing adoption in industries like healthcare and finance for automation.
- Efficiency in Model Training: New techniques are reducing costs and improving accessibility.
- Ethical & Regulatory Challenges: Ongoing concerns around responsible AI development.
"""

SUMMARY_EXAMPLE = COMPLETE_EMAIL + EMAIL_SUMMARY
