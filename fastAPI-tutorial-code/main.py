from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

class Message(BaseModel):
    text: str
    sender: str

@app.post("/echo")
def echo_message(message: Message):
    return {
        "received": message.text,
        "from": message.sender,
        "response": f"Echo: {message.text}"
    }