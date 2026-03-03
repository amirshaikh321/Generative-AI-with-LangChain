# What is a Prompt in LangChain?
**🧠 Simple Definition**<br>
A Prompt is the instruction or input template that tells the LLM what to do.<br>
It is how you control the behavior of the model.

`model.invoke("Explain AI")`<br>
this works.<br>But it’s not structured.

.

## 🔷 With Proper Prompt
Explain Artificial Intelligence in 3 bullet points for beginners.

Now the output is:
- Structured
- Controlled
- Clear

That instruction = Prompt


🔷 In LangChain: PromptTemplate

LangChain allows you to create dynamic prompts using templates.

Instead of hardcoding:<br>
> "Explain Machine Learning"

You can create a reusable template:

> from langchain_core.prompts import PromptTemplate
> 
> prompt = PromptTemplate.from_template(
>     "Explain {topic} in simple terms."
> )
> 
> formatted_prompt = prompt.invoke({"topic": > "Machine Learning"})
> print(formatted_prompt)

Output sent to model:
> Explain Machine Learning in simple terms.

## 🔷 Types of Prompts in LangChain
- PromptTemplate
- ChatPromptTemplate
