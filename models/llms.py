from langchain_openai import ChatOpenAI
from configs import MODEL_CONFIGS


class LLMSelector:
    """
    通用多模型选择器，初始化时传入模型名，只需url、apikey、modelname即可。
    所有模型配置由config.py中的MODEL_CONFIGS维护。
    """
    def __init__(self, modelname: str):
        if modelname not in MODEL_CONFIGS:
            raise ValueError(f"未找到模型: {modelname}")
        self.config = MODEL_CONFIGS[modelname]
        self.modelname = modelname
    

    def _select(self):
        llm = ChatOpenAI(
            model=self.modelname,
            base_url=self.config["base_url"],
            api_key=self.config["api_key"],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"]
        )
        return llm


    def __call__(self):
        # 让实例像函数一样直接返回模型
        return self._select()
    