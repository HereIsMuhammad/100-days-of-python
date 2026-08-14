"""
Day 84: FastAPI Basics & Routing
Requires: pip install fastapi "uvicorn[standard]"
Run with: uvicorn Day84-FastAPIBasics:app --reload
(rename the file to remove hyphens if uvicorn complains about the module name,
 e.g. Day84_FastAPIBasics.py)
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Day 84 Demo API")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# In-memory "database" just for this demo
items_db: dict[int, Item] = {}
next_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Day 84 FastAPI demo!"}


@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    all_items = list(items_db.items())
    return dict(all_items[skip: skip + limit])


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    return items_db[item_id]


@app.post("/items")
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    created = {"id": next_id, **item.model_dump()}
    next_id += 1
    return created


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    removed = items_db.pop(item_id, None)
    if removed is None:
        return {"error": "Item not found"}
    return {"deleted": item_id}
