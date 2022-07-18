from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None


app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


items = [
    Item(name="pencil", price=1.99),
]


@app.get("/")
def read_root():
    return {"ping": "OK :^)"}


@app.get("/items")
async def read_items():
    return items
