"""
Day 85: REST API Development — Books API
Requires: pip install fastapi "uvicorn[standard]"
Run with: uvicorn Day85_RESTAPI:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books REST API")


class BookIn(BaseModel):
    title: str
    author: str
    year: int


class BookOut(BookIn):
    id: int


books_db: dict[int, BookIn] = {
    1: BookIn(title="Clean Code", author="Robert C. Martin", year=2008),
    2: BookIn(title="Fluent Python", author="Luciano Ramalho", year=2015),
}
next_id = 3


@app.get("/books", response_model=list[BookOut])
def list_books():
    return [BookOut(id=book_id, **book.model_dump()) for book_id, book in books_db.items()]


@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    book = books_db.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookOut(id=book_id, **book.model_dump())


@app.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookIn):
    global next_id
    books_db[next_id] = book
    result = BookOut(id=next_id, **book.model_dump())
    next_id += 1
    return result


@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookIn):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = book
    return BookOut(id=book_id, **book.model_dump())


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
