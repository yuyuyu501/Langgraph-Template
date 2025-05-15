from dotenv import load_dotenv
import os

# 程序启动时自动加载 .env 文件
load_dotenv()

def getenv(key, default=None):
    return os.getenv(key, default)


MODEL_CONFIGS = {
    "mistralai/mistral-small-3.1-24b-instruct:free": {
        "name": "mistralai/mistral-small-3.1-24b-instruct:free",
        "base_url": "https://openrouter.ai/api/v1",
        "api_key": getenv("OPENROUTER_API_KEY"),
        "max_tokens": 10000,
        "temperature": 0.5
    },
}