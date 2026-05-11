import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub

import boto3
import requests

load_dotenv()

# Get the credentials from environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
aws_region = os.getenv("AWS_REGION")
weatherstack_access_key = os.getenv("WEATHERSTACK_ACCESS_KEY")

search_tool = DuckDuckGoSearchRun()

# results = search_tool.run("top news about hantavirus?")

# print(results)

@tool()
def get_weather_data(city: str) -> str:
    """
    Get the current weather data for a given city using the Weatherstack API.
    """
    url = f'https://api.weatherstack.com/current?access_key={weatherstack_access_key}&query={city}'

    response = requests.get(url)
    data = response.json()
    return data

# Initialize the Bedrock client
client = boto3.client(
    "bedrock-runtime",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
    )

model_kwargs = {
    "temperature": 0.7,
    "max_tokens": 1000
}

# Initialize the ChatBedrock LLM
llm = ChatBedrock(
    provider="anthropic",
    model="us.anthropic.claude-sonnet-4-6",
    model_kwargs=model_kwargs,
    client=client
)

# print(llm.invoke('hi'))

# Agent creation
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# wrap agent in with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

# Run the agent
response = agent_executor.invoke(
    {"input": "what is the capital of madhya pradesh and what is the weather there?"}
)

# print(response)

print(response['output'])