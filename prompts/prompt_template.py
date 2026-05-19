from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = PromptTemplate(
    template="Greet this person in 5 langauges. The name of the person is {name}.",
    input_variables=["name"]
)

prompt = template.invoke(input={"name": "Alice"})

result = model.invoke(prompt)

print(result.content)
