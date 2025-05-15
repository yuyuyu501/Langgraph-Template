from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from models import get_llm
from tools import tools
from langgraph.prebuilt import ToolNode


class State(TypedDict):
    messages: Annotated[list, add_messages]

def get_agent(modelname):
    llm = get_llm(modelname)
    llm_with_tools = llm.bind_tools(tools)

    def chatbot(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    tool_node = ToolNode(tools=tools)

    return chatbot, tool_node