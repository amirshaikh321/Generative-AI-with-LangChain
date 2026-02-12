from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

code = """from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load document
loader = TextLoader("royal_enfield_gt_650.txt", encoding="utf-8")
documents = loader.load()

# Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " "]
)

chunks = text_splitter.split_documents(documents)

# Output
print(f"Total chunks: {len(chunks)}")
print(chunks[0].page_content)
"""
text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 250,
    chunk_overlap = 0)

result = text_splitter.split_text(text=code)

print(result[1])