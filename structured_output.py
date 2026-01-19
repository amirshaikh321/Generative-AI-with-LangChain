from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict, Annotated
from dotenv import load_dotenv
load_dotenv()
# 1. Define your schema (Pydantic)
class MovieReview(TypedDict):
    title: Annotated[str,"The title of the movie"]
    sentiment: Annotated[str, "The sentiment of the review (Positive/Negative)"]
    rating: Annotated[int,"A rating out of 10"]

# 2. Setup the Base LLM (Using Hugging Face Inference API)
# We use a model known for good instruction following, like Llama-3 or Mixtral
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

# 3. Wrap it in ChatHuggingFace
# This wrapper adds the "chat" structure required for structured output
chat_model = ChatHuggingFace(llm=llm)

# 4. Bind the structure
# Note: For non-function-calling models, this often relies on prompt engineering/JSON mode
structured_llm = chat_model.with_structured_output(MovieReview)

# 5. Invoke
result = structured_llm.invoke("I just watched Inception and it was mind-blowing! A solid 9.")

print(result)
# Expected Output:
# title='Inception' sentiment='Positive' rating=9