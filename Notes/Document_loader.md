# Document Loaders in LangChain

## What are Document Loaders?

**Definition:**

Document Loaders in LangChain are components used to load data from different sources such as files, websites, PDFs, databases, or APIs and convert them into a standardized **Document format** that LangChain can process.

In simple terms:

> Data Source → Document Loader → LangChain Document Objects


---

# Why Document Loaders Are Important

Large Language Models (LLMs) cannot directly access external data sources like:

- PDFs
- Text files
- Websites
- CSV files
- Databases

Document loaders help retrieve and prepare this data so it can be used in AI applications such as:

- Retrieval-Augmented Generation (RAG)
- Question answering systems
- Chatbots
- Knowledge assistants

---

# LangChain Document Object

After loading, data is converted into a **Document object**.

A document typically contains:

- **page_content** → actual text content  
- **metadata** → additional information about the document

Example structure:

```python
Document(
    page_content="LangChain is a framework for building LLM applications.",
    metadata={"source": "file.txt"}
)