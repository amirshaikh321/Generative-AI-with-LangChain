from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


st.header("AutoInfo AI 🚗🏍️")

user_input = st.text_input("Ask what info you want about cars and bikes.")


tempelate = PromptTemplate(
    template="""You are an expert automobile assistant specializing in cars and bikes.

Your responsibilities:
- Provide accurate and simple explanations
- Answer only vehicle-related questions
- Compare vehicles when asked
- Suggest vehicles based on budget and usage
- Explain technical terms in easy language

If the question is unrelated to cars or bikes, politely refuse.

Answer format:
- Clear headings
- Bullet points where needed
- Short and user-friendly responses

Question: {question}

""",
input_variables=['question']
)

prompt = tempelate.invoke({
    'question': user_input
})


if st.button('⚡ Run AI'):
    result = model.invoke(prompt)
    st.write(result.content)
