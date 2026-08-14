# Day 84: FastAPI Basics & Routing

## Setup
```bash
pip install fastapi "uvicorn[standard]"
```
`fastapi` is the framework; `uvicorn` is the ASGI server that runs it.

## Your First App
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```
Run it with:
```bash
uvicorn main:app --reload
```
Then visit `http://127.0.0.1:8000` and the auto-generated docs at
`http://127.0.0.1:8000/docs`.

## Path Parameters
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```
FastAPI uses the type hint (`int`) to validate and convert the URL segment
automatically — if someone passes `/users/abc`, FastAPI returns a 422 error.

## Query Parameters
```python
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```
Call: `/items?skip=5&limit=20`

## Request Body with Pydantic
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create_item(item: Item):
    return {"received": item}
```
Pydantic models validate incoming JSON automatically — wrong types get
rejected with a clear error message before your function even runs.

## Route by HTTP Method
```python
@app.get("/items/{id}")     # read
@app.post("/items")         # create
@app.put("/items/{id}")     # replace
@app.patch("/items/{id}")   # partial update
@app.delete("/items/{id}")  # delete
```

## Summary
FastAPI routes map URLs + HTTP methods to Python functions. Type hints
give you free request validation and interactive docs — a big productivity
win over manually parsing HTTP requests.
