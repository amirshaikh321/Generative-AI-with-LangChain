from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vectors = embedding.embed_documents(docs)

print(f"Number of vectors generated: {len(vectors)}") 
print(f"Dimension of each vector: {len(vectors[0])}")
print(f"First vector (start): {str(vectors[0])[:50]}...")