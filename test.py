from core import Chat
from utils import chunk_filting

if __name__ == "__main__":
    idx = '1030'
    modelname = "mistralai/mistral-small-3.1-24b-instruct:free"
    mode = "stream"
    messages = "Can you give me a script for a health video on Douyin?"
    chat = Chat(modelname, mode)
    result = chat.chat(messages, idx)
    if mode == "stream":
        for chunk in result:
            chunk = chunk_filting(chunk)
            print(chunk, end="", flush=True)
        print()
    else:
        print(result)