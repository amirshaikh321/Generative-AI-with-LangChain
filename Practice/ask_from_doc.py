import streamlit as st
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import CSVLoader, PyPDFLoader, TextLoader, Docx2txtLoader
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
prompt = PromptTemplate(
    template='Answer the following questions \n{question}\nfrom this data: \n{data}',
    input_variables=['question','data']
)
parser = StrOutputParser()

chain = prompt | model | parser

st.set_page_config(page_title="Ai", page_icon="📁")

st.title("Ask From documents")

uploaded_file = st.file_uploader(
    "📂 Upload Your Document",
    type=["csv", "pdf", "txt", "docx"]
)
UPLOAD_DIR = "uploaded_files"
Path(UPLOAD_DIR).mkdir(exist_ok=True)

if uploaded_file:
    file_path = Path(UPLOAD_DIR) / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

question = st.text_input(
    "💬 Ask a Question from Your File",
    placeholder="e.g. What is Topic of Document"
)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run = st.button("🤖 Analyze Document", use_container_width=True)


if run and uploaded_file is not None:
    # File details
    file_name = uploaded_file.name
    file_extension = Path(file_name).suffix.lower()
    file_size = uploaded_file.size

    if file_extension == '.csv':
        loader = CSVLoader(file_path=str(file_path))
        docs = loader.load()
        result = chain.invoke({'question':question,'data':docs})
        st.success('Answer')
    if file_extension == '.pdf':
        loader = PyPDFLoader(file_path=str(file_path))
        docs = loader.load()
        result = chain.invoke({'question':question,'data':docs})
        st.success('Answer')
    if file_extension == '.txt':
        loader = TextLoader(file_path=str(file_path))
        docs = loader.load()
        result = chain.invoke({'question':question,'data':docs})
        st.success('Answer')
    if file_extension == '.docs':
        loader = Docx2txtLoader(file_path=str(file_path))
        docs = loader.load()
        result = chain.invoke({'question':question,'data':docs})
        st.success('Answer')

    st.markdown(result)
