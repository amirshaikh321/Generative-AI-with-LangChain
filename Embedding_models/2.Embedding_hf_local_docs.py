from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2')

docs= ["Delhi is the captital of India",
       "kolkata is the capital of west bengal",
       "paris is the capital of France"]

vector = embedding.embed_query(docs)

print(str(vector))