from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import crud

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/analysis")
async def get_analysis(review: str):
    # TODO
    return crud.analysis(review)


@app.get("/emotions/{id}")
async def get_emotions(id: int):
    return crud.get_emotions(id)


@app.get("/nouns/{id}")
async def get_nouns(id: int):
    return crud.get_nouns(id)


@app.get("/phrases/{id}")
async def get_phrases(id: int):
    return crud.get_phrases(id)
