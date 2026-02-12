from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='Text_splitter\RCB_IPL_Emotion.pdf')

docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 50,
                                      chunk_overlap = 5,
                                      separator='')

result = text_splitter.split_documents(docs)
print(result[0].page_content)