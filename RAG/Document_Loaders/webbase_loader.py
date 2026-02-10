from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following questions \n {question}\n from this text: \n{text}',
    input_variables=['question','text']
)

chain = prompt | model | parser
url = "https://en.wikipedia.org/wiki/KTM"
loader = WebBaseLoader(url)
docs = loader.load()
question = input('Ask Question : \n')
result = chain.invoke({'question':question, 'text': docs})
print(result)
