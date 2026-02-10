from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'Document_Loaders\Documents',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs= loader.load()

print(f"Length of document : {len(docs)}\n")
print(f"Page Content of first page: {docs[0].page_content}\n")
print(f"Metadata of first page : {docs[0].metadata}")