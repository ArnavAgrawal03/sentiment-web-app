from fastapi import FastAPI
from pydantic import BaseModel
import sentiment
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Score(BaseModel):
    # different types of scores
    positive: float
    negative: float
    neutral: float
    compound: float


# this works for a single word, but we want to be able to pass in a sentence
@app.get("/sentiment/q?={sentence}")
def route_query(sentence: str) -> Score:
    result = sentiment.getSentiment(sentence)
    return Score(
        positive=result["pos"],
        negative=result["neg"],
        neutral=result["neu"],
        compound=result["compound"]
    )
    
