from langchain_core.prompts import ChatPromptTemplate

chat_tempelate = ChatPromptTemplate([
    ('system', 'you are expert in {domain}'),
    ('human', 'what is {topic}')
])

chat_history = chat_tempelate.invoke({'domain':'machine learning','topic':'supervised learning'})

print(chat_history)