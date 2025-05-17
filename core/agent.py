from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from models import get_llm
from tools import tools
from langgraph.prebuilt import ToolNode



class State(TypedDict):
    messages: Annotated[list, add_messages]


class AgentBuilder:
    def __init__(self, modelname: str):
        self.llm = get_llm(modelname)
        self.llm_with_tools = self.llm.bind_tools

    def get_agent(self):
        def chatbot(state: State):
            return {"messages": [self.llm_with_tools.invoke(state["messages"])]}

        tool_node = ToolNode(tools=tools)

        return chatbot, tool_node