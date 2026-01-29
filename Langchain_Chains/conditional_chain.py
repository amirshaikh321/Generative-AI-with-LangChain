from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

class feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser = PydanticOutputParser(pydantic_object=feedback)
parser1= StrOutputParser()
prompt1 = PromptTemplate(
    template='Classify the sentiment of following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
classiifier_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template = (
    "Write a friendly, genuine, and professional reply to the positive feedback below. dont give options of the reply "
    "Thank the person and acknowledge their appreciation without sounding repetitive.\n\n"
    "Feedback:\n{feedback}"
),
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = (
    "Write a polite, empathetic, and professional response to the negative feedback below. dont give options of the response"
    "Acknowledge the concern, apologize if appropriate, and show willingness to improve or resolve the issue "
    "without being defensive.\n\n"
    "Feedback:\n{feedback}"
),
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser1),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser1),
    RunnableLambda( lambda x: 'could not find sentiment')
)

final_chain = classiifier_chain | branch_chain

result = final_chain.invoke({'feedback':'this is a terrible phone'})
print(result)
final_chain.get_graph().print_ascii()