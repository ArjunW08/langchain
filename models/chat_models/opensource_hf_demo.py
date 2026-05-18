from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation"
)

model = ChatHuggingFace(llm=endpoint)

result = model.invoke("What is the capital of France?")

print(result.content)