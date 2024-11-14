from fastapi import FastAPI
from pydantic import BaseModel

class Hello(BaseModel):
    name: str

app = FastAPI()    

@app.get("/hello/{param}")
# put body and param inside the parameter in the function
async def hello(item:Hello, param):
    return {
        "message": f"Hello {item.name} {param}"
    }