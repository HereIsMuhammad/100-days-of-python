# Day 99: Capstone Project — Testing & Refactoring

## Goal for This Phase
Add a real test suite for the Expense Tracker API (Day 98) using `pytest`
(Day 79) and FastAPI's `TestClient`, then refactor for cleanliness.

## Testing FastAPI Apps
FastAPI ships with a `TestClient` (built on `httpx`) that lets you call
your API directly in tests, without running a live server.
```bash
pip install httpx pytest
```
```python
from fastapi.testclient import TestClient
from myapp import app

client = TestClient(app)

def test_register_and_login():
    response = client.post("/register", json={"username": "test", "password": "pass123"})
    assert response.status_code == 201

    response = client.post("/login", data={"username": "test", "password": "pass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
```

## Using a Separate Test Database
Never run tests against your real database! Override the `get_db`
dependency to point at a temporary SQLite database (or `:memory:`).
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

test_engine = create_engine("sqlite:///./test.db")
TestSession = sessionmaker(bind=test_engine)

def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
```

## Testing Authenticated Routes
```python
def get_auth_headers(client, username, password):
    client.post("/register", json={"username": username, "password": password})
    response = client.post("/login", data={"username": username, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_expense():
    headers = get_auth_headers(client, "ali", "secret123")
    response = client.post("/expenses", json={
        "amount": 50.0, "date": "2026-08-14", "category_id": 1
    }, headers=headers)
    assert response.status_code == 201
```

## Refactoring Checklist
Once tests pass, look for opportunities to clean up:
- Extract repeated logic (like `get_auth_headers`) into shared fixtures.
- Move magic strings/numbers into named constants.
- Split an overgrown `main.py` into `routes/`, `models.py`, `schemas.py`
  files if it hasn't been already (Day 97's architecture).
- Add docstrings to functions that aren't self-explanatory.

## Why Test Before Refactoring?
A solid test suite is what makes refactoring **safe** — if tests still
pass after restructuring code, you know behavior didn't change even
though the code's internal shape did.

## Summary
Testing with `TestClient` + a dedicated test database validates the
capstone's behavior end-to-end (auth, categories, expenses) without ever
touching production data, and gives the confidence needed to refactor
freely.
