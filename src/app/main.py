from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PingPong(BaseModel):
    message: str
    
@app.get("/ping")
async def pong():

    return {"ping": "pong!"}


@app.post("/what_is_ping")
async def ping_to_pong(pingpong_message: PingPong):
    if pingpong_message.message.lower() == "ping":
        return_message = {"ret_message":"Pong!"}
    else:
        return_message = {"ret_message":"No Ping so no Pong!"}

    return return_message
