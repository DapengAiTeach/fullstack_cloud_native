import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    response = requests.get("http://ch06_demo05_api:8000/ping")
    return {"data": response.json()}