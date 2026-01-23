from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id='MiniMaxAI/MiniMax-M2.1',
    task='text-generation',
    device='cuda',
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens=100
    ))
model = ChatHuggingFace(llm=llm)

result = model.invoke('what is currency of india')
print(result.content)
