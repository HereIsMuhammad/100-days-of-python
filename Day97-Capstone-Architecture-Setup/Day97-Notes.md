# Day 97: Capstone Project — Architecture & Setup

## The Capstone: Personal Expense & Budget Tracker API
To wrap up the 100 days, we build one complete project that pulls together
almost everything learned: OOP (Days 43-56), file/DB handling (Days 32,
64-66, 87), FastAPI + auth (Days 83-89), testing (Days 78-79), data tools
(Days 90-93), and packaging/CI (Days 94-96).

## Feature Scope
- User registration & JWT login.
- Users can create expense categories (Food, Rent, Transport, ...).
- Users can log expenses against a category with amount, date, and note.
- Users can view a monthly summary (total spent, spend by category).
- A `/analytics` endpoint returns data ready for charting (ties to
  Pandas/Matplotlib from Days 91-93).

## Architecture
```
capstone_project/
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── main.py          # FastAPI app & routes
│       ├── models.py        # SQLAlchemy models
│       ├── schemas.py       # Pydantic request/response schemas
│       ├── auth.py          # JWT + password hashing
│       ├── database.py      # engine/session setup
│       └── analytics.py     # Pandas-based summary logic
├── tests/
│   └── test_expenses.py
├── .github/workflows/tests.yml
├── pyproject.toml
└── README.md
```

Each concern lives in its own file — this is a **layered architecture**:
routes call into database/auth helpers rather than one giant file doing
everything, which mirrors how real production backends are organized.

## Data Model (planned)
```
User
 ├── id, username, hashed_password
 └── expenses (1-to-many)

Category
 ├── id, name
 └── expenses (1-to-many)

Expense
 ├── id, amount, note, date
 ├── owner_id -> User
 └── category_id -> Category
```

## Setup Plan for This Phase (Day 97)
1. Scaffold the folder structure above (using the packaging pattern from
   Day 94).
2. Define `pyproject.toml` with dependencies: fastapi, uvicorn,
   sqlalchemy, python-jose, passlib, pandas, pytest.
3. Define the SQLAlchemy models (`User`, `Category`, `Expense`) and create
   the database tables.
4. Confirm the database file & tables are created correctly before
   building any routes (Day 98).

## Summary
Good architecture upfront — clear separation between models, schemas,
auth, and routes — makes the rest of the capstone (Days 98-100) far
easier to build, test, and extend.
