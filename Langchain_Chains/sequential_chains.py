from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template=('Give me the detailed report on {topic}'),
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template=('Generate a 5 pointer summary on the following \n {text}'),
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke({'topic': 'Bollywood industry'})
print(response)
chain.get_graph().print_ascii()