# Retrievers in LangChain

## What is a Retriever?

**Definition:**

A **Retriever** in LangChain is a component that retrieves the most relevant documents from a data source (usually a vector store) based on a user query.

In simple terms:

User Query → Retriever → Relevant Documents


The retriever searches stored documents and returns the ones most related to the query.

---

# Why Retrievers Are Important

Large Language Models (LLMs) do not have direct access to external knowledge sources such as:

- PDFs
- Databases
- Websites
- Internal documents

Retrievers solve this problem by fetching relevant documents and providing them to the LLM.

This is the foundation of **Retrieval-Augmented Generation (RAG)**.

---

# How Retrievers Work

Documents
↓
Text Splitter
↓
Embeddings
↓
Vector Store
↓
Retriever
↓
Relevant Documents
↓
LLM
↓
Answer


The retriever acts as the **search system** in this pipeline.

---

| Feature  | Vector Store      | Retriever                    |
| -------- | ----------------- | ---------------------------- |
| Role     | Stores embeddings | Retrieves relevant documents |
| Function | Database          | Search interface             |
| Input    | Embeddings        | User query                   |
| Output   | Stored vectors    | Relevant documents           |


# Basic Example of a Retriever

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

texts = [
    "LangChain is a framework for building LLM applications.",
    "Machine learning enables computers to learn from data.",
    "Python is widely used in AI development."
]

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_texts(texts, embedding=embeddings)

retriever = vectorstore.as_retriever()

docs = retriever.invoke("What is LangChain?")

print(docs)
