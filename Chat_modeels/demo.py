# chat_tinyllama.py

from langchain.chat_models import HuggingFaceChat
from langchain.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables (e.g., HUGGINGFACEHUB_API_TOKEN)
load_dotenv()

# Make sure your Hugging Face API token is set
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HF_TOKEN:
    raise ValueError("Please set your HUGGINGFACEHUB_API_TOKEN in a .env file")

# Step 1: Initialize the LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # TinyLlama 1.1B Chat
    task="text-generation",
    huggingfacehub_api_token=HF_TOKEN
)

# Step 2: Wrap it in a Chat model
chat_model = HuggingFaceChat(llm=llm)

# Step 3: Invoke the chat
prompt = "Who is the best actor in India?"
response = chat_model.invoke(prompt)

# Step 4: Print the response
print("Response:", response.content)
