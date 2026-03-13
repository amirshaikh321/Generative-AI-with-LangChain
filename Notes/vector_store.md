# Vector Stores in LangChain

## What is a Vector Store?

**Definition:**

A **Vector Store** is a database used to store **vector embeddings** of text so that similar pieces of information can be quickly retrieved using similarity search.

In simple terms:

> Text → Embedding Model → Vector → Vector Store


The vector store allows the system to **search for semantically similar content** instead of exact keyword matches.

---

# Why Vector Stores Are Needed

Large Language Models cannot remember large datasets directly.

Vector stores help by:

- Storing document embeddings
- Performing similarity search
- Retrieving relevant information for LLMs
- Enabling **Retrieval-Augmented Generation (RAG)**

Example:

User Question:

What is LangChain?


Vector store finds documents **semantically similar** to the question.

---

# What is an Embedding?

Before storing data in a vector store, text must be converted into **embeddings**.

Embedding = numerical representation of text.

Example:
> "LangChain is an AI framework"


may become:

[0.23, -0.91, 0.44, 0.67, ...]


These numbers represent the **semantic meaning** of the text.

---

# How Vector Stores Work

Documents<br>
↓<br>
Text Splitter<br>
↓<br>
Embedding Model<br>
↓<br>
Vector Store<br>
↓<br>
Similarity Search<br>
↓<br>
Relevant Documents

---

# Basic Example in LangChain

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_texts(
    ["LangChain is a framework for LLM applications"],
    embedding=embeddings
)