from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """# Engine
GT 650 uses a 648cc parallel twin engine.

# Design
The motorcycle follows a café racer design.
"""
text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 75,
    chunk_overlap = 0)

result = text_splitter.split_text(text=code)

print(result[1])