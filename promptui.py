from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2",
                          task="text-generation")

model = ChatHuggingFace(llm=llm)

st.header("BrainBox 🤖")

prompt = st.text_input("Enter your prompt.")

if st.button("Run"):
    result = model.invoke(prompt)
    st.write(result.content)
