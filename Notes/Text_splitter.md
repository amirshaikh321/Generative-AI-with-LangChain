# Text Splitters in LangChain

## What is a Text Splitter?

**Definition:**

A **Text Splitter** in LangChain is a component used to divide large documents into smaller chunks of text so that they can be processed efficiently by language models.

Large Language Models (LLMs) have **token limits**, so long documents must be split before processing.

> Large Document → Text Splitter → Small Chunks


---

# Why Text Splitting is Important

LLMs cannot handle very large texts due to **context window limitations**.

Example:

- GPT models have token limits (e.g., 8k, 32k, etc.)
- A large PDF may contain thousands of words

Text splitters help:

- Break large documents into manageable chunks
- Improve retrieval accuracy in RAG systems
- Reduce token usage
- Enable efficient embedding generation

---

# Example Without Text Splitting

PDF (200 pages)<br>
↓<br>
LLM<br>

Problems:

- Too many tokens
- Slow processing
- Poor retrieval

---

# Example With Text Splitting

PDF<br>
↓<br>
Document Loader<br>
↓<br>
Text Splitter<br>
↓<br>
Chunks of Text<br>
↓<br>
Embeddings<br>
↓<br>
Vector Database<br>

---

# Basic Example of Text Splitter

```python
from langchain_text_splitters import CharacterTextSplitter

text = "LangChain is a framework for building applications with large language models."

splitter = CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=5
)

chunks = splitter.split_text(text)

print(chunks)