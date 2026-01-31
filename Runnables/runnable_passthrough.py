from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke on a {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Give me Explination about of following joke {text}',
    input_variables=['text']
)

first_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'Explination': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(first_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})
print(result)
