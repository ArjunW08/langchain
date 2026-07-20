from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langsmith import Client

search_tool = DuckDuckGoSearchRun()

load_dotenv()

@tool
def get_weather_data(city: str) -> str:
    """
    This Function fetaches the current weather data for a given city
    """

    url = f'https://api.weatherstack.com/current?access_key=70affe774a9229c3ad09ace9e0b5af9a&query={city}'

    response = requests.get(url)

    return response.json()


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

client = Client()
prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})

print(response['output'])

