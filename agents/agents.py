from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_experimental.utilities import PythonREPL
from langchain_core.tools import Tool

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OpenAIGPT4OMini = ChatOpenAI(model="gpt-4o", temperature=0.7)

python_repl = PythonREPL()
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)

internal_tools = [repl_tool]

coding_agent = Agent(
    role="Python Data Analyst",
    goal="Analyze data and provide insights using Python",
    backstory="You are an experienced data analyst with strong Python skills.",
    tools=internal_tools,
    allow_delegation=False,
    verbose=True,
    llm=OpenAIGPT4OMini,
)