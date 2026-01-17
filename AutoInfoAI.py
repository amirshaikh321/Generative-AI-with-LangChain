from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.2",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
chat_history = []
st.markdown("""
<h1 style='text-align: center;'>🚗 AutoInfo AI 🏍️</h1>
<p style='text-align: center; color: gray;'>
Your smart assistant for cars & bikes information, comparisons, and buying advice
</p>
""", unsafe_allow_html=True)


user_input = st.text_input(
    "Ask about cars & bikes",
    placeholder="e.g. Compare Honda City vs Hyundai Verna"
)

tempelate = load_prompt('tempelate.json')

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run = st.button("⚡ Run AI", use_container_width=True)


if run and user_input:
    chat_history.append(user_input)
    with st.spinner("AutoInfo AI is thinking..."):
        chain = tempelate | model
        result = chain.invoke({
    'question': user_input
})
        st.success("Answer generated ✅")
        st.markdown(result.content)

if run and not user_input:
    st.warning("Please enter a question about cars or bikes 🚘")
