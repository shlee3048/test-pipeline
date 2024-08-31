from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Hello World API
@app.get("/hello")
async def hello():
    return "Hello World"


class EchoText(BaseModel):
    text: str

# Echo API
@app.post("/echo")
async def echo(echo_text:EchoText):
    return f"[{echo_text.text}] is received!!!"
