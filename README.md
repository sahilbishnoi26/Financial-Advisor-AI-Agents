# Multi-Agent Financial & Web Research System

## Description
This project demonstrates how to create and orchestrate multiple AI agents—one specialized in financial analysis and another in web research using **OpenAIChat (gpt-4o-mini)** to provide context-aware, natural language responses.

## Features
- **Financial Analyst Agent**: Fetches real-time stock data, fundamentals, and analyst recommendations using `YFinanceTools`.
- **Web Research Agent**: Gathers fresh information via `DuckDuckGo`.
- **Agent Teaming**: Multiple agents can collaborate and combine insights in a single response.
- **OpenAIChat (gpt-4o-mini)**: Provides conversation-based interaction and summarization.

## Technologies Used
- **Phi**: For creating, orchestrating, and configuring AI agents.
- **OpenAIChat (gpt-4o-mini)**: AI model for generating text-based responses and performing NLP tasks.
- **YFinanceTools**: Fetches stock prices, analyst recommendations, and fundamental data from Yahoo Finance.
- **DuckDuckGo**: Tool for searching the web and retrieving the latest information.
- **Python**: The main programming language driving the solution logic.

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
   - Open your main Python file (e.g., `main.py`) to edit model IDs, instructions, or tool settings as necessary.

2. **Run the Project**  
   - `python main.py`  
   - This starts the agents. One agent pulls financial data, and the other performs web searches.  

3. **Interact with the Agents**  
   - Within your code, you can call:  
     ```python
     agents_team.print_response("Compare Nvidia and Tesla stocks, give recommendations")
     ```
   - The output will include comparison tables, references from DuckDuckGo, and any relevant financial details.

## Troubleshooting
- **Issue**: Failure to Retrieve Stock Data  
  - **Solution**: Check your internet connection and confirm `YFinanceTools` is installed.
- **Issue**: Web Search Tool Error  
  - **Solution**: Ensure there are no firewall restrictions blocking DuckDuckGo.
- **Issue**: Incorrect or Missing Model ID  
  - **Solution**: Verify that `OpenAIChat(id="gpt-4o-mini")` is correctly referenced and any required API keys are properly set.
- **Issue**: Script Fails to Run  
  - **Solution**: Make sure the virtual environment is activated and dependencies are installed (`pip install -r requirements.txt`).
