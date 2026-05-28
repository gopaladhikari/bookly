from fastapi import FastAPI, Header
from typing import Union
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
