from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke on a {topic}',
    input_variables=['topic']
)

joke_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel({
    'Joke':RunnablePassthrough(),
    'Word_count':RunnableLambda(lambda x:len(x.split()))
})

final__chain = RunnableSequence(joke_chain, parallel_chain)
result  = final__chain.invoke({'topic':'AI'})

str_result = """ Joke : \n{}\nWord count: \n{}""".format(result['Joke'],result['Word_count'])
print(str_result)