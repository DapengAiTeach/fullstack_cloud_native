from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def info():
    return {
        "hostname": socket.gethostname()
    }