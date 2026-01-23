from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
                          repo_id="deepseek-ai/DeepSeek-V3.2",
                          task='text-generation')

model = ChatHuggingFace(llm= llm)


schema = [
    ResponseSchema(name = 'fact_1', description = 'fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description = 'fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description = 'fact 3 about the topic'),
    ResponseSchema(name = 'fact_4', description = 'fact 4 about the topic'),
    ResponseSchema(name = 'fact_5', description = 'fact 5 about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give 5 facts about the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

response = chain.invoke({})
print(response)