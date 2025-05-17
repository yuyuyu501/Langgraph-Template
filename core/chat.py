from core import AgentBuilder, GraphBuilder
from models import output_factory, gen_prompt
from utils import chunk_filting
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')



class ChatBuilder:
    def __init__(self, modelname: str="mistralai/mistral-small-3.1-24b-instruct:free", mode: str="stream"):
        try:
            logging.info(f"初始化Chat，模型: {modelname}，模式: {mode}")
            self.modelname = modelname
            self.modelname = modelname
            self.mode = mode
            self.agent = AgentBuilder(self.modelname)

            self.chatbot, self.tool_node = self.agent.get_agent()
            self.graphbuilder = GraphBuilder(self.chatbot, self.tool_node)
            self.graph = self.graphbuilder.get_graph()
            self.output_handler = output_factory(mode)

        except Exception as e:
            logging.error(f"Chat初始化失败: {e}", exc_info=True)
            raise

    
    def chat(self, user_input: str, idx: str="1"):
        return self._process_chat(user_input, idx)

    def _process_chat(self, user_input: str, idx: str="1"):
        config = {"configurable": {"thread_id": idx}}
        try:
            message = gen_prompt(user_input)
            response = self.output_handler.gen_handle(self.graph, message, config)
            return response
        except Exception as e:
            logging.error(f"对话处理异常: {e}", exc_info=True)
            return "对话过程中发生异常，请稍后重试。"


if __name__ == "__main__":
    idx = '1030'
    modelname = "mistralai/mistral-small-3.1-24b-instruct:free"
    mode = "stream"
    messages = "Can you give me a script for a health video on Douyin?"
    chat = ChatBuilder(modelname, mode)
    result = chat.chat(messages, idx)
    if mode == "stream":
        for chunk in result:
            chunk = chunk_filting(chunk)
            print(chunk, end="", flush=True)
        print()
    else:
        print(result)