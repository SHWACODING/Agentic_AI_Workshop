from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

while True:
    user_input = input("======== AI Agent ======== \n\nAsk Your Question : ")
    
    if user_input == "exit" or user_input == "quit":
        break
    
    agent_team.print_response(user_input)

# e.g. Analyze companies like Tesla, NIVDIA, Apple and suggest which to buy for long term
