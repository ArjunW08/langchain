from langchain_classic.agents import initialize_agent, AgentType
from langchain_core.tools import InjectedToolArg
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from typing import Annotated
from dotenv import load_dotenv
import requests

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

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

agent_executor = initialize_agent(
    tools = [get_conversion_factor, convert],
    llm = model,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # using ReAct pattern
    verbose=True  # shows internal thinking
)

user_query = " "
while(user_query):
    print("Enter your query")
    user_query = input()

    if user_query == "exit":
        print("Bye")
        break

    response = agent_executor.invoke({"input": user_query})
    print(response)