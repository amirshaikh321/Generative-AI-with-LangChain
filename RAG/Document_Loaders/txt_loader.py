from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Give the summary of the document \n {docs}",
    input_variables=['docs']
)

loader = TextLoader('Document_Loaders\Documents\machine_learning.txt',encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser 
print(chain.invoke({'docs':docs[0].page_content}))