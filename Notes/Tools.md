# Tools in LangChain

## What are Tools in LangChain?

**Definition:**

Tools in LangChain are functions or external capabilities that a language model can use to perform specific tasks such as searching the web, querying a database, performing calculations, or calling APIs.

In simple terms:

User Query → LLM → Tool → Result


Tools extend the abilities of a language model beyond text generation.

---

# Why Tools Are Needed

Large Language Models have limitations:

- They cannot perform real-time calculations
- They cannot access live data
- They cannot interact with external systems directly

Tools solve these limitations by allowing the LLM to interact with external systems.

Examples:

- Web search
- Database queries
- Weather APIs
- Calculators
- File operations


The LLM decides **which tool to use** based on the user query.

---

# Example of a Simple Tool

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b