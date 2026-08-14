"""
Day 99: Capstone Project — Testing & Refactoring
Test suite for the Day 98 Expense Tracker backend.
Requires: pip install fastapi httpx sqlalchemy python-jose[cryptography] passlib[bcrypt] pytest
Run with: pytest Day99-CapstoneTesting.py
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the app + dependency + Base from Day 98
# (rename Day98-CapstoneBackend.py to Day98_CapstoneBackend.py locally
#  to import it as a normal Python module, since filenames can't contain hyphens)
from Day98_CapstoneBackend import app, get_db, Base


# --- Use an isolated, temporary test database instead of the real one ---
test_engine = create_engine("sqlite:///./test_day99.db", connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
Base.metadata.create_all(bind=test_engine)


def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def get_auth_headers(username="testuser", password="secret123"):
    client.post("/register", json={"username": username, "password": password})
    response = client.post("/login", data={"username": username, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_register_creates_user():
    response = client.post("/register", json={"username": "alice", "password": "pass123"})
    assert response.status_code == 201


def test_register_duplicate_username_fails():
    client.post("/register", json={"username": "bob", "password": "pass123"})
    response = client.post("/register", json={"username": "bob", "password": "different"})
    assert response.status_code == 400


def test_login_returns_token():
    client.post("/register", json={"username": "charlie", "password": "pass123"})
    response = client.post("/login", data={"username": "charlie", "password": "pass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_wrong_password_fails():
    client.post("/register", json={"username": "dave", "password": "pass123"})
    response = client.post("/login", data={"username": "dave", "password": "wrongpass"})
    assert response.status_code == 401


def test_create_category_requires_auth():
    response = client.post("/categories", json={"name": "Groceries"})
    assert response.status_code == 401


def test_create_and_list_category():
    headers = get_auth_headers("erin", "secret123")
    response = client.post("/categories", json={"name": "Travel"}, headers=headers)
    assert response.status_code == 201

    response = client.get("/categories")
    names = [c["name"] for c in response.json()]
    assert "Travel" in names


def test_create_expense_rejects_negative_amount():
    headers = get_auth_headers("frank", "secret123")
    client.post("/categories", json={"name": "Bills"}, headers=headers)
    categories = client.get("/categories").json()
    category_id = categories[0]["id"]

    response = client.post("/expenses", json={
        "amount": -10, "date": "2026-08-14", "category_id": category_id
    }, headers=headers)
    assert response.status_code == 422  # Pydantic validator rejects it


def test_create_and_list_expense():
    headers = get_auth_headers("grace", "secret123")
    cat_response = client.post("/categories", json={"name": "Health"}, headers=headers)
    category_id = cat_response.json()["id"]

    response = client.post("/expenses", json={
        "amount": 75.5, "date": "2026-08-14", "category_id": category_id, "note": "Doctor visit"
    }, headers=headers)
    assert response.status_code == 201

    response = client.get("/expenses", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1
