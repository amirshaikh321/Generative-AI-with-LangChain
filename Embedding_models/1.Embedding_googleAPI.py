from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004')

text= "Delhi is the captital of India"

vector = embedding.embed_query(text)

print(str(vector))