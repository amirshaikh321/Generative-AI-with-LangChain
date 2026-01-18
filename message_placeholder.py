from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
chat_temp = ChatPromptTemplate([
    ('system','you are expert assistent'),
    MessagesPlaceholder("chat_history"),
    ('human','{querry}')
])
chat_history = []
with open('chat_history.txt','r')as f:
    chat_history.extend(f.readlines())

prompt = chat_temp.invoke({'chat_history':chat_history, 'querry': 'what is status of my refund'})
print(prompt)