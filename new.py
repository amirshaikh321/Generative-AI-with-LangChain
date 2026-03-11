import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")
parser = StrOutputParser()
# response = model.invoke("who is pm of india")

st.header("This is ai")

que = st.text_input(
    "Ask any question"
)
chain = model | parser

if st.button("Run"):
    response = chain.invoke(que)
    st.markdown(response)
