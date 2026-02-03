import streamlit as st
from pathlib import Path

st.set_page_config(page_title="File Upload Demo", page_icon="📁")

st.title("📁 File Upload Demo")

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["csv", "pdf", "txt", "docx"]
)

if uploaded_file is not None:
    # File details
    file_name = uploaded_file.name
    file_extension = Path(file_name).suffix.lower()
    file_size = uploaded_file.size

    st.success("File uploaded successfully!")

    st.write("### File Info")
    st.write("**Name:**", file_name)
    st.write("**Extension:**", file_extension)
    st.write("**Size (bytes):**", file_size)
