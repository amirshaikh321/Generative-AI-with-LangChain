from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = CSVLoader(file_path='Document_Loaders\Documents\std.csv')
docs = loader.load()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt = PromptTemplate(
    template='Answer the following questions \n{question}\nfrom this data: \n{data}',
    input_variables=['question','data']
)
parser= StrOutputParser()

chain = prompt | model | parser
question = input('Ask question: \n')
result = chain.invoke({'question': question, 'data':docs})
print(result)
