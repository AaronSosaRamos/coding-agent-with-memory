from typing import Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessagesState
from langgraph.prebuilt import ToolNode

from tools.tools import tools

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

model = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)

# Define the function that determines whether to continue or not
def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    # If the LLM makes a tool call, then we route to the "tools" node
    if last_message.tool_calls:
        return "tools"
    # Otherwise, we stop (reply to the user)
    return END


# Define the function that calls the model
def call_model(state: MessagesState):
    messages = state['messages']
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}

tool_node = ToolNode(tools)