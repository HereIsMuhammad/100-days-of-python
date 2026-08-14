# Day 88: FastAPI & Database Integration

## Goal
Connect the FastAPI skills from Days 84-86 with the SQLAlchemy skills from
Day 87, so API endpoints read/write real database rows instead of
in-memory Python dicts.

## Database Setup File (`database.py` pattern)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

## Dependency Injection for DB Sessions
FastAPI's `Depends()` provides a fresh session per request and closes it
afterward automatically:
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Using it in a Route
```python
from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users")
def create_user(user: UserIn, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

## Separating Pydantic Schemas from SQLAlchemy Models
- **SQLAlchemy model** (`models.py`) → defines the database table.
- **Pydantic schema** (`schemas.py`) → defines the API's request/response
  shape.

This separation means you can change your API's public shape without
touching your database structure, and vice versa.

```python
class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True   # allows creating from a SQLAlchemy object
```

## Summary
The `Depends(get_db)` pattern is the standard way to give each request its
own database session in FastAPI, keeping the database layer decoupled and
testable.
