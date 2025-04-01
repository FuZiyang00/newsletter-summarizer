# Email summary 
simple program that fetches unread emails and use an LLM to produce summaries for each of them 

## Workflow 
1. Fetching emails content:
    - email ID, 
    - sender, 
    - body. 

2. Restructuring emails' body to make them suitable to be digested by an LLM; 

3. Feeding the restructured emails to the LLM.

> [!WARNING]  
> **For Gmail:** you need to set up the project in *Google Cloud Platform* to obtain the API credentials json file. 

## Sources
https://murraycole.com/posts/gmail-auto-labeler-llm 


## Project structure
```
project-root/
|── .gitub/
│ └── workflows/
│       └── CI.yml
│
├── scrips/
│ ├── __init__.py
│ ├── constants.py
│ ├── gmail_client.py
| ├── llm.py
| ├── prompts.py
| └── utisl.py
|
├── pipelines/
│ ├── gmail_client_pipeline.py
│ └── llm_response_pipeline.py
│ 
├── Makefil
├── main.py
├── requirements.txt
└── README.md
```