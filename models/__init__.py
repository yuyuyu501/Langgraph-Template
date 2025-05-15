from .llms import LLMSelector
from .prompt import gen_prompt
from .stream_output import output_factory


def get_llm(modelname):
    return LLMSelector(modelname)()

