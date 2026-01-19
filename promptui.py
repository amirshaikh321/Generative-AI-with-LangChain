from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
                          task="text-generation")

model = ChatHuggingFace(llm=llm)

st.header("BrainBox 🤖")

prompt = st.text_input("Enter your prompt.")

if st.button("Run"):
    result = model.invoke(prompt)
    st.write(result.content)
