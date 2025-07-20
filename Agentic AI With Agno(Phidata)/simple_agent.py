from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an assistant please reply based ont he question",
    tools=[DuckDuckGoTools()],
    markdown=True
)


while True:
    user_input = input("======== AI Agent ======== \n\nAsk Your Question : ")
    
    if user_input == "exit" or user_input == "quit":
        break
    
    agent.print_response(user_input)
