# Agents in LangChain

## What are Agents?

**Definition:**

Agents in LangChain are components that allow a language model to **dynamically decide which actions or tools to use in order to complete a task**.

Unlike simple chains that follow a fixed pipeline, agents can **reason, choose tools, and perform multiple steps** before producing the final answer.

User Query → Agent → Decide Action → Use Tool → Observe Result → Final Answer


---

# Why Agents Are Needed

Chains follow a **fixed workflow**, but real-world problems require flexibility.

Example problem:

"What is the square root of the population of India?"


Steps required:

1. Get population of India
2. Calculate square root

A fixed chain cannot easily handle this.

An **Agent can decide the steps dynamically**.

---

# How Agents Work

Agents follow a loop called the **Reasoning-Action Cycle**.

User Question<br>
↓<br>
Agent (LLM)<br>
↓<br>
Reasoning<br>
↓<br>
Select Tool<br>
↓<br>
Execute Tool<br>
↓<br>
Observe Result<br>
↓<br>
Repeat if Needed<br>
↓<br>
Final Answer<br>


This process allows the agent to solve complex problems step by step.

---

# Components of an Agent

| Component | Description |
|----------|-------------|
| LLM | The reasoning engine |
| Tools | External capabilities (APIs, calculators, etc.) |
| Prompt | Instructions guiding the agent |
| Agent Executor | Runs the agent loop |

---

# Example of Tools Used by an Agent

Tools may include:

- Calculator
- Web search
- Database queries
- File operations
- API calls

Example tools list:

```python
tools = [calculator_tool, weather_tool]

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import Tool

llm = ChatOpenAI()

tools = [
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Useful for math calculations"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What is 12 * 8?")