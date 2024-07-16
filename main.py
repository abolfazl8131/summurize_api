from scenarios import summurize_the_text

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Body(BaseModel):
    text: str
    

@app.post("/sumurrize_the_text/")
async def summurize_text(body:Body):
    return {"message": summurize_the_text(body.text)}


