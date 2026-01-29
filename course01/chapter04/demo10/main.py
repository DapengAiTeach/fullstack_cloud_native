from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "fastapi_base_image_running"}