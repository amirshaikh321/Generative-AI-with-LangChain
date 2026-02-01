from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')

parser = StrOutputParser()

prompt1= PromptTemplate(
    template='Write a report on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the given text less than 300 words \n {text}',
    input_variables=['text']
)

report_chain = RunnableSequence(prompt1,model,parser)

summarize_chain = RunnableBranch(
    (lambda x: len(x.split()) >= 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final = report_chain | summarize_chain
print(final.invoke({'topic':'JAVA vs Python'}))