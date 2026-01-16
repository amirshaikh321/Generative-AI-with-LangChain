from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

st.header("AutoInfo AI 🚗🏍️")

querry = st.text_input("Ask what info you want about cars and bikes.")

if st.button('⚡ Run AI'):
    result = model.invoke(querry)
    st.write(querry)
    