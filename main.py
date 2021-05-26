from typing import Optional
from fastapi import FastAPI
import crud

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analysis")
async def get_analysis(review: str):
    # TODO
    return crud.get_emotions(id)


@app.get("/emotions/{id}")
async def get_emotions(id: int):
    return crud.get_emotions(id)


@app.get("/nouns/{id}")
async def get_nouns(id: int):
    return crud.get_nouns(id)


@app.get("/phrases/{id}")
async def get_phrases(id: int):
    return crud.get_phrases(id)
