# Multi-Agent Financial & Web Research System

## Description
This project demonstrates how to create and orchestrate multiple AI agents—one specialized in financial analysis and another in web research—using **OpenAIChat (gpt-4o-mini)** to provide context-aware, natural language responses. The code also includes optional support for open-source models from Groq, which can be uncommented and configured as needed.

## Features
- **Financial Analyst Agent**: Fetches real-time stock data, fundamentals, and analyst recommendations using `YFinanceTools`.
- **Web Research Agent**: Gathers fresh information via `DuckDuckGo`.
- **Agent Teaming**: Multiple agents collaborate to combine insights into a unified response.
- **Customizable AI Models**: Supports OpenAIChat (`gpt-4o-mini`) and optional open-source models from Groq (`llama-3.3-70b-versatile`).
- **Dynamic Questions**: Easily modify the query to get responses tailored to your needs.

## Technologies Used
- **Phi**: For creating, orchestrating, and configuring AI agents.
- **OpenAIChat (gpt-4o-mini)**: AI model for generating text-based responses and performing NLP tasks.
- **Groq**: Optional support for open-source models such as `llama-3.3-70b-versatile`.
- **YFinanceTools**: Fetches stock prices, analyst recommendations, and fundamental data from Yahoo Finance.
- **DuckDuckGo**: Tool for searching the web and retrieving the latest information.
- **Python**: The primary programming language driving the solution logic.

## Installation
1. **Clone the Repository**  
   - `git clone https://github.com/your-username/multi-agent-financial-web-research.git`
   - `cd multi-agent-financial-web-research`

2. **Create and Activate a Virtual Environment**  
   - On Windows:  
     - `python -m venv venv`  
     - `venv\Scripts\activate`
   - On macOS/Linux:  
     - `python3 -m venv venv`  
     - `source venv/bin/activate`

3. **Install Dependencies**  
   - `pip install -r requirements.txt`

## Usage
1. **Configure Agents**  
   - Open `financial_agents.py` to edit model configurations, tools, or instructions. Uncomment the Groq model line to use an open-source model (`Groq(id="llama-3.3-70b-versatile")`).

2. **Modify the Query**  
   - Update the question in `agents_team.print_response()` to ask what you'd like. For example:
     ```python
     agents_team.print_response("Compare Nvidia and Tesla stocks, give recommendations")
     ```

3. **Run the Project**  
   - Run the script:
     ```bash
     python financial_agents.py
     ```

## Troubleshooting
- **Issue**: Failure to Retrieve Stock Data  
  - **Solution**: Check your internet connection and confirm `YFinanceTools` is installed.
- **Issue**: Web Search Tool Error  
  - **Solution**: Ensure there are no firewall restrictions blocking DuckDuckGo.
- **Issue**: Incorrect or Missing Model ID  
  - **Solution**: Verify the model ID (`gpt-4o-mini` or `llama-3.3-70b-versatile`) and ensure any required API keys are properly set.
- **Issue**: Script Fails to Run  
  - **Solution**: Make sure the virtual environment is activated and dependencies are installed (`pip install -r requirements.txt`).

Enjoy using this Multi-Agent System for financial analysis and web research!
