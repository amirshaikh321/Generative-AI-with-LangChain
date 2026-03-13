# Retrieval-Augmented Generation (RAG)

## What is RAG?

**Definition:**

Retrieval-Augmented Generation (RAG) is a technique that combines **information retrieval** with **large language models (LLMs)** to generate responses based on external knowledge sources.

Instead of relying only on the model’s training data, RAG retrieves relevant documents from a database and provides them as context to the LLM before generating a response.

User Query → Retrieve Documents → LLM Generates Answer


---

# Why RAG is Needed

Large Language Models have limitations:

- They cannot access **private or real-time data**
- They may produce **hallucinations**
- Their knowledge is limited to **training data**

RAG solves these problems by allowing LLMs to use **external knowledge sources** such as:

- PDFs
- Websites
- Databases
- Company documents
- Knowledge bases

---

# Step-by-Step Explanation

### 1. Document Loading
Documents are loaded from sources like PDFs, text files, or websites.

### 2. Text Splitting
Large documents are divided into smaller chunks.

### 3. Embeddings
Each chunk is converted into numerical vectors using an embedding model.

### 4. Vector Store
These embeddings are stored in a vector database.

### 5. Retrieval
When a user asks a question, the retriever finds the most relevant document chunks.

### 6. Generation
The LLM uses the retrieved documents as context to generate the final answer.

---

LLM generates the final answer using the retrieved context.

---

# Basic Example in LangChain

```python
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)

response = qa_chain.invoke("What is LangChain?")
print(response)