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


# creating a file search stoe

file_search_store = client.file_search_stores.create(config={'display_name':"MLH_DOCS"})

print(f"Created store: {file_search_store.name}")  # This is the "search store name" (long ID)

#Upload our files to the file search store
files = [
    "C:\\Users\\HP\\OneDrive\\Documents\\PracticePy\\Oreilly ML\\HACKATHON\\docs\\MLH NEWS.txt",
    "C:\\Users\\HP\\OneDrive\\Documents\\PracticePy\\Oreilly ML\\HACKATHON\\docs\\MLH_ORG.txt",
    "C:\\Users\\HP\\OneDrive\\Documents\\PracticePy\\Oreilly ML\\HACKATHON\\docs\\MLH_POLICY.txt"
]

file_search_store_name = file_search_store.name
if not file_search_store_name:
    raise ValueError("Failed to create file search store - name is None")
for file in files:
    operation = client.file_search_stores.upload_to_file_search_store(
        file = file,
        file_search_store_name=file_search_store_name,
        config = {
            'display_name': file.split("/")[-1]
        }

    )

    while not operation.done:
        time.sleep(2)
        operation = client.operations.get(operation)

    print(f"File {file} uploaded successfully")

    





