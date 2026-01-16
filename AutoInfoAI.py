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
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run = st.button("⚡ Run AI", use_container_width=True)


if run and user_input:
    with st.spinner("AutoInfo AI is thinking..."):
        result = model.invoke(prompt)
        st.success("Answer generated ✅")
        st.markdown(result.content)

if run and not user_input:
    st.warning("Please enter a question about cars or bikes 🚘")
