from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="what is the ANN in following text \n {docs}",
    input_variables=['docs']
)

loader = PyPDFLoader('Document_Loaders\Documents\Detailed_Deep_Learning_Report.pdf')

docs = loader.load()

chain = prompt | model | parser 
print(chain.invoke({'docs':docs[0].page_content}))