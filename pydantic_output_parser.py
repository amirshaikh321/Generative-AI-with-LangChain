from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2",
                          task='text-generation')
model = ChatHuggingFace(llm= llm)

class Person(BaseModel):

    name : str = Field(description='Name of the Person')
    age : int = Field(gt = 18, description='age of the person')
    city : str = Field(description='name of city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template1 = PromptTemplate(
    template="Generate the name, age, city of a fictional {place} Person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({'place':'nepal'})
print(result)