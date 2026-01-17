from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-V3.2',
                          task='text-generation')
model = ChatHuggingFace(llm=llm)
chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input('you:')
    if user_input == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    print("AI:",result.content)
    chat_history.append(AIMessage(content=result.content))
