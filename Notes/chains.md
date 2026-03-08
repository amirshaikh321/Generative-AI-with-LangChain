# 🔷 What are Chains in LangChain?

### 🧠 Definition

A Chain in LangChain is a sequence of components that are connected together so the output of one step becomes the input of the next step.

It creates a workflow for LLM applications.

Instead of manually doing:

`User Input → Prompt → LLM → Process Output`

LangChain lets you chain these steps together.

### 🔷 Example Workflow

User Question
      ↓
Prompt Template
      ↓
Chat Model
      ↓
Output Parser
      ↓
Final Structured Output

## Types of Chains in LangChain

1️⃣ Simple Chain (Prompt → Model)

2️⃣ Sequential Chain

3️⃣ Parallel Chain

4️⃣ Router Chain
