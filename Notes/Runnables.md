# Runnables in LangChain

## What are Runnables?

**Definition:**

A **Runnable** in LangChain is a standard interface that represents any component capable of taking an input, processing it, and returning an output.

In simple terms:
> Input → Runnable → Output


Examples of runnables in LangChain include:

- Prompt Templates
- Chat Models
- Output Parsers
- Retrievers
- Tools
- Chains

All these components follow the same runnable interface.

---

# Why LangChain Introduced Runnables

Earlier versions of LangChain used many different classes such as:

- `LLMChain`
- `SequentialChain`
- `RouterChain`

This made the framework complex.

Modern LangChain introduced **Runnables** to unify all components under a single execution interface.

Now every component can be executed using the same methods.

---

# Core Runnable Methods

| Method | Purpose |
|------|------|
| `invoke()` | Run the runnable once |
| `batch()` | Run with multiple inputs |
| `stream()` | Stream the output |
| `ainvoke()` | Run asynchronously |

---

## Example: invoke()

```python
response = chain.invoke({"topic": "LangChain"})