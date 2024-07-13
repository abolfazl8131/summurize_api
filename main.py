from scenarios import summurize_the_text

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Body(BaseModel):
    text: str
    


@app.post("/sum/")
async def summurize(body:Body):
    return {"message": summurize_the_text(body.text)}


