from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv

load_dotenv()



model = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-001'
)

semantic = SemanticChunker(
    embeddings=model,
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=1.5
)
text = """
The engine of the Continental GT 650 is a 648cc parallel-twin unit that produces
strong mid-range torque and smooth power delivery. It is paired with a 6-speed
gearbox and a slipper clutch, making highway cruising and city riding comfortable.
The engine is known for its reliability and refined performance.

In recent years, artificial intelligence has transformed the way people interact
with technology. AI-powered systems are now used in healthcare, finance, education,
and transportation to automate tasks and improve decision-making.
Machine learning models learn patterns from data and continuously improve
their predictions over time.

Cloud computing has further accelerated the adoption of AI by providing scalable
infrastructure and on-demand resources. Platforms such as AWS, Google Cloud, and
Azure enable developers to deploy AI applications globally without managing"""

result = semantic.split_text(text=text)

print(result[0])