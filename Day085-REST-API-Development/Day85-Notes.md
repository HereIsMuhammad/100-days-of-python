# Day 85: REST API Development

## What Makes an API "RESTful"?
REST (Representational State Transfer) is a set of conventions:
- Resources are identified by **URLs** (`/users`, `/users/5`).
- Standard HTTP methods express actions (GET, POST, PUT, PATCH, DELETE).
- Responses use standard status codes (200, 201, 404, ...).
- The API is stateless — each request contains everything the server needs.

## Designing Good Endpoints
| Action | Method | URL |
|---|---|---|
| List all books | GET | `/books` |
| Get one book | GET | `/books/{id}` |
| Create a book | POST | `/books` |
| Update a book fully | PUT | `/books/{id}` |
| Update a book partially | PATCH | `/books/{id}` |
| Delete a book | DELETE | `/books/{id}` |

Use **nouns**, not verbs, in URLs: `/books` not `/getBooks`.

## Status Codes to Return
```python
from fastapi import FastAPI, HTTPException, status

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    ...

@app.get("/books/{id}")
def get_book(id: int):
    if id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[id]
```

## Structuring a Larger API with `APIRouter`
```python
from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/")
def list_books():
    ...

# In main.py
app.include_router(router)
```
This keeps routes organized by feature/resource instead of one giant file.

## Response Models
```python
class BookOut(BaseModel):
    id: int
    title: str

@app.get("/books/{id}", response_model=BookOut)
def get_book(id: int):
    ...
```
`response_model` filters/validates the output shape, hiding internal fields.

## Summary
A well-designed REST API is predictable: consistent URL patterns, correct
HTTP methods, and meaningful status codes make it easy for any client to
use without reading extensive documentation.
