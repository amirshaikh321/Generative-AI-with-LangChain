from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

JSON_schema = {
  "title": "MovieReview",
  "type": "object",
  "properties": {
    "title": {
      "title": "Title",
      "description": "The title of the movie",
      "type": "string"
    },
    "sentiment": {
      "title": "Sentiment",
      "description": "The sentiment of the review (Positive/Negative)",
      "type": "string"
    },
    "rating": {
      "title": "Rating",
      "description": "A rating out of 10",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "sentiment",
    "rating"
  ]
}

sturctured_model = model.with_structured_output(JSON_schema)

result = sturctured_model.invoke("I just watched Inception and it was mind-blowing! A solid 9.")

print(result)