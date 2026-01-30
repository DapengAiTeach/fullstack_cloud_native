from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/ping")
def ping():
    return {
        "status": "ok",
        "hostname": socket.gethostname()
    }