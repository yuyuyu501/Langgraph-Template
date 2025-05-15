from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage

# 静态提示词
system_message = SystemMessage(content="永远说中文")


# 动态提示词
human_template = HumanMessagePromptTemplate.from_template("{question}")

prompt_template = ChatPromptTemplate.from_messages([
    system_message,
    human_template,
])

def gen_prompt(question):
    prompt = prompt_template.format_prompt(
        question=question,
    ).to_messages()
    # 只返回当前消息
    return prompt

if __name__ == '__main__':
    print(system_message)
    print(gen_prompt(question = "你好吗？"))
