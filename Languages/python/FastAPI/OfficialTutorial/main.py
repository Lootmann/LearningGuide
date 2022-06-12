from fastapi import FastAPI

my_app = FastAPI()

db = {
    1: {
        "name": "pencil",
        "price": 1.99,
    },
    2: {
        "name": "eraser",
        "price": 0.99,
    },
}


@my_app.get("/")
async def root():
    return db


@my_app.get("/items/{item_id}")
async def read_item(item_id: int):
    return db.get(item_id, "NoItem")
