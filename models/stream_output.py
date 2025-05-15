from abc import ABC, abstractmethod
import logging


class BaseOutputHandler(ABC):
    @abstractmethod
    def gen_handle(self, graph, messages, config):
        """处理events，返回内容。"""
        pass



class StreamOutputHandler(BaseOutputHandler):
    def gen_handle(self, graph, messages, config):
        """流式输出"""
        try:
            for msg_chunk, metadata in graph.stream(
                input={"messages": messages}, 
                config=config,
                stream_mode="messages"
            ):
                yield msg_chunk.content
        except Exception as e:
            logging.error(f"流式输出异常: {e}", exc_info=True)
            raise
        



class StandardOutputHandler(BaseOutputHandler):
    def gen_handle(self, graph, messages, config):
        """标准输出"""
        try:
            result = graph.invoke(
                input={"messages": messages},
                config=config,
            )
            if hasattr(result, "content"):
                return result.content
            elif hasattr(result, "messages"):
                return "".join([msg.content for msg in result.messages if hasattr(msg, "content")])
            else:
                return str(result)
        except Exception as e:
            logging.error(f"标准输出异常: {e}", exc_info=True)
            raise



def output_factory(mode="stream"):
    if mode == "stream":
        return StreamOutputHandler()
    else:
        return StandardOutputHandler()


