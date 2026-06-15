from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# tool create
@tool
def multiply(a: int, b: int):
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

print("Tool Details\n")
print(f"Name : {multiply.name}\n")
print(f"Description : {multiply.description}\n")
print(f"Arguments : {multiply.args}\n")

# tool binding
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

print(f"{llm.invoke('Hi')}\n")

llm_with_tool = llm.bind_tools([multiply])

print(f"{llm_with_tool.invoke('Hi, can you perform mathematical operations?')}\n")

query = HumanMessage('Can you multiply 4 with 25')

messages = [query]

print(f"Formed message : {messages}\n")

result = llm_with_tool.invoke(messages)

messages.append(result)

print(f"Current Message Stream : {messages}\n")

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

print(f"Total messages : {len(messages)}\n")

print(f"Current Message Stream : {messages}\n")

print(f"Answer : {llm_with_tool.invoke(messages).content}")
