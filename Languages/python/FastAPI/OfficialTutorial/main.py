from fastapi import FastAPI

my_app = FastAPI()

db = {
    0: {
        "name": "ruler",
        "price": 2.15,
    },
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


# query parameters
@my_app.get("/items/")
async def item_range(start_id: int = 0, end_id: int = 0):
    if start_id > end_id:
        return {"message": "id needs start < end"}

    if start_id == 0 and end_id == 0:
        return db

    ret = {}
    for i in range(start_id, end_id + 1):
        if i in db:
            ret.update({i: db[i]})

    return ret


# path prameters
@my_app.get("/items/{item_id}")
async def read_item(item_id: int):
    return db.get(item_id, "NoItem")
