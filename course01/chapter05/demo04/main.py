from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "fastapi-network-demo",
        "hostname": socket.gethostname(),
        "time": datetime.utcnow().isoformat()
    }