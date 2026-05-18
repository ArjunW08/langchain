from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")

result = model.invoke("What is the capital of France?", temperature=0.7, max_completion_tokens=100)

print(result.content)

# Process is same for other models from anthropic's claude, gemini, etc.