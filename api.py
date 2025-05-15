from fastapi import FastAPI
from routers.chatrouter import router
import uvicorn



app = FastAPI()
app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
