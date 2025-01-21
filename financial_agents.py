from phi.agent import Agent  # Importing the Agent class for creating AI agents.
from phi.model.groq import Groq  # Optional Groq model for open-source AI capabilities
from phi.model.openai import OpenAIChat  # Importing OpenAIChat model for natural language processing tasks.
from phi.tools.duckduckgo import DuckDuckGo  # Tool for conducting web-based searches using DuckDuckGo.
from phi.tools.yfinance import YFinanceTools  # Tool for retrieving financial data via Yahoo Finance.

# Define the Financial Analyst agent
financial_agent = Agent(
    name="Financial Analyst",  # The name of the agent for identification and role definition.
    # model=Groq(id="llama-3.3-70b-versatile"),  # Optional open-source Groq model
    model=OpenAIChat(id="gpt-4o-mini"),  # Using OpenAIChat for natural language responses.
    tools=[  # Adding tools specific to financial analysis tasks.
        YFinanceTools(
            stock_price=True,  # Enables fetching real-time stock price data.
            analyst_recommendations=True,  # Enables retrieving analyst recommendations for stocks.
            stock_fundamentals=True  # Enables retrieving stock fundamentals (e.g., P/E ratio, market cap).
        )
    ],
    show_tool_calls=True,  # Enables logging of tool usage for transparency and debugging.
    markdown=True,  # Outputs the agent's responses in Markdown format for improved readability.
    instructions=["Always create tables for comparisons"],  # Specific guidelines for the agent's outputs.
)

# Define the Web Researcher agent
web_researcher = Agent(
    name="Web Researcher",  # The name of the agent for identification and role definition.
    # model=Groq(id="llama-3.3-70b-versatile"),  # Optional open-source Groq model
    model=OpenAIChat(id="gpt-4o-mini"),  # Using OpenAIChat for natural language responses.
    tools=[DuckDuckGo()],  # Adding DuckDuckGo for conducting web-based research.
    show_tool_calls=True,  # Enables logging of tool usage for transparency and debugging.
    markdown=True,  # Outputs the agent's responses in Markdown format for improved readability.
    instructions=["Always include sources of the information that you gather"],  # Specific guidelines for sourcing information.
)

# Combine both agents into a collaborative team
agents_team = Agent(
    team=[financial_agent, web_researcher],  # A team consisting of the Financial Analyst and Web Researcher agents.
    # model=Groq(id="llama-3.3-70b-versatile"),  # Optional open-source Groq model
    model=OpenAIChat(id="gpt-4o-mini"),  # Using OpenAIChat to orchestrate team responses.
    show_tool_calls=True,  # Enables logging of tool usage for transparency and debugging.
    markdown=True,  # Outputs the team's responses in Markdown format for improved readability.
    instructions=[  # Combined instructions for the team to ensure consistent outputs.
        "Always include source of the information gathered", 
        "Always create tables for comparisons"
    ],
    debug_mode=True  # Enables debug mode for detailed logs of the agents' operations.
)

# Query the agents team to get a response
# The query requests a summary of Nvidia's analyst recommendations and the latest information.
agents_team.print_response("Summarise the analyst recommendations and share the latest information about Nvidia?")
