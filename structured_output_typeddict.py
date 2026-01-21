from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
load_dotenv()

class MovieReview(TypedDict):
    title: Annotated[str,"The title of the movie"]
    sentiment: Annotated[str, "The sentiment of the review (Positive/Negative)"]
    rating: Annotated[int,"A rating out of 10"]

chat_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

structured_llm = chat_model.with_structured_output(MovieReview)
result = structured_llm.invoke("I just watched Inception and it was mind-blowing! A solid 9.")

print(result)