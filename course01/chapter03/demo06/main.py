import os
from fastapi import FastAPI

app = FastAPI()

# 开发模式
ENV = os.getenv("ENV", "development")


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "env": ENV,
    }
