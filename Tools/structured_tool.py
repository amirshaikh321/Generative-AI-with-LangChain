from langchain_core.tools import StructuredTool
from pydantic import Field, BaseModel

class MultiplyInput(BaseModel):
    a:int = Field(required = True, description='The first number to add')
    b:int = Field(required = True, description='The Second number to add')

def multiply(a : int, b: int) -> int: 
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description='Multiply two numbers',
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':22, 'b':32 })
print(result)