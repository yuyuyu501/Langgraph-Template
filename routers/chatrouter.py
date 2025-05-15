from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from core import Chat
import logging



router = APIRouter()

class ChatRequest(BaseModel):
    user_input: str
    idx: str = "1"
    modelname: str = "mistralai/mistral-small-3.1-24b-instruct:free"
    mode: str = "stream"

# 全局单例
chat_engine = Chat(modelname="mistralai/mistral-small-3.1-24b-instruct:free", mode="stream")

@router.post("/chat")
def chat_api(request: ChatRequest):
    try:
        result = chat_engine.chat(request.user_input, request.idx)
        if request.mode == "stream":
            # 流式输出
            def event_stream():
                for chunk in result:
                    yield chunk
            return StreamingResponse(event_stream(), media_type="text/event-stream")
        else:
            # 标准输出
            return StreamingResponse((f"data: {result}\n\n",), media_type="text/event-stream")
    except Exception as e:
        logging.error(f"chat接口异常: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="AI对话服务异常，请稍后重试。")