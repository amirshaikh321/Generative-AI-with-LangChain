# 🔷 What are Output Parsers in LangChain?

## 🧠 Definition

Output Parsers are components in LangChain that convert the raw text output from an LLM into a structured format such as JSON, lists, dictionaries, or Pydantic objects.

## 🔴 Without Output Parser

LLM Output:

> John is 25 years old and works as a software engineer.

Hard for a program to extract:
* Name
* Age
* Profession

## 🟢 With Output Parser

Parsed Output:

`{
  "name": "John",
  "age": 25,
  "profession": "Software Engineer"
}`

# 🔷 Common Types of Output Parsers in LangChain
* 1️⃣ StrOutputParser (Most Basic)
* 2️⃣ JSON Output Parser
* 3️⃣ Pydantic Output Parser
* 4️⃣ CommaSeparatedListOutputParser
