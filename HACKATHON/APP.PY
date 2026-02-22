'''
SESSION PLAN:
Intro to gemini file search api
get gmini api key
prepare documents for rag
setup Document for RAG
Setup RAG Pipeline
    Import Documents
    Query Gemini File Search API
Create UI
'''

#the first step is to get gemini running locally
from dotenv import load_dotenv
import os
from google import genai
import time

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


        