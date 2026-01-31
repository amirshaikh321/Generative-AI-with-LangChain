from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a funny joke"
)

prompt2 = PromptTemplate(
    template="write and explain the given following joke \n {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = chain.invoke({})
print(result)