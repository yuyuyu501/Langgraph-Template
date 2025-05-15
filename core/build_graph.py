from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from databases.memory import memory
from .agent import *
import logging


class GraphBuilder:
    def __init__(self, chatbot, tool_node):
        try:
            logging.info("初始化GraphBuilder")
            self.chatbot = chatbot
            self.tool_node = tool_node
            self.graph_builder = StateGraph(State)
        except Exception as e:
            logging.error(f"GraphBuilder初始化失败: {e}", exc_info=True)
            raise

    def _add_node(self):
        try:
            self.graph_builder.add_node("chatbot", self.chatbot)
            self.graph_builder.add_node("tools", self.tool_node)
            logging.info("节点添加完成")
        except Exception as e:
            logging.error(f"添加节点失败: {e}", exc_info=True)
            raise

    def _add_edge(self):
        try:
            self.graph_builder.add_edge(START, "chatbot")
            self.graph_builder.add_conditional_edges("chatbot", tools_condition)
            self.graph_builder.add_edge("tools", "chatbot")
            self.graph_builder.add_edge("chatbot", END)
            logging.info("边添加完成")
        except Exception as e:
            logging.error(f"添加边失败: {e}", exc_info=True)
            raise

    def get_graph(self):
        try:
            self._add_node()
            self._add_edge()
            graph = self.graph_builder.compile(checkpointer=memory)
            logging.info("Graph构建完成")
            return graph
        except Exception as e:
            logging.error(f"Graph构建失败: {e}", exc_info=True)
            raise