from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """Artificial intelligence is changing how people work and learn.
Small ideas grow into powerful systems when data, logic, and creativity come together.
Sometimes progress is fast, sometimes it pauses, but innovation never really stops.
Technology keeps rewriting the rules of what is possible.
"""
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100,
                                               chunk_overlap = 5)

result = text_splitter.split_text(text=text)

print(result[1])