from langchain_core.tools import InjectedToolArg
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from typing import Annotated
from dotenv import load_dotenv
import json
import requests
# from langchain.agents import create_agent for future use.

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base curreny 
    and a target currency.
    """

    url = f'https://v6.exchangerate-api.com/v6/api_key/pair/{base_currency}/{target_currency}'

    response = requests.get(url)

    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    given a currency converison rate this function calculates the target currency value 
    from a given base currency value.
    """

    return base_currency_value * conversion_rate


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        pieces = []
        for item in content:
            if isinstance(item, dict):
                pieces.append(str(item.get('text', '')))
            else:
                pieces.append(str(item))
        return '\n'.join([p for p in pieces if p])
    if isinstance(content, dict):
        return str(content.get('text', content))
    return str(content)

conversion_factor_response = get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency' : 'INR'})

print(conversion_factor_response)

# tool binding
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage("What is the conversion factor between INR and USD, and based on that can you convert 100 INR to USD?")]

print(f"Current message stream : {messages}\n")

ai_message = llm_with_tools.invoke(messages)

conversion_rate = None
step = 1
while True:
    print(f"Step {step} AI response content: {ai_message.content!r}")
    print(f"Step {step} AI tool calls: {ai_message.tool_calls}\n")

    if not ai_message.tool_calls:
        print(f"Answer : {extract_text(ai_message.content)}")
        break

    messages.append(ai_message)
    for tool_call in ai_message.tool_calls:
        if tool_call['name'] == 'get_conversion_factor':
            tool_message1 = get_conversion_factor.invoke(tool_call)
            print(f"Executed get_conversion_factor -> {tool_message1.content}\n")
            messages.append(tool_message1)
            conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        elif tool_call['name'] == 'convert':
            if conversion_rate is not None:
                tool_call['args']['conversion_rate'] = conversion_rate
            tool_message2 = convert.invoke(tool_call)
            print(f"Executed convert -> {tool_message2.content}\n")
            messages.append(tool_message2)

    print(f"Current message stream : {messages}\n")
    ai_message = llm_with_tools.invoke(messages)
    step += 1