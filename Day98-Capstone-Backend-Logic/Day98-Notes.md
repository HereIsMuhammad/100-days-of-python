# Day 98: Capstone Project — Backend & Logic

## Goal for This Phase
Build on Day 97's data model by adding the actual FastAPI application:
authentication routes plus full CRUD for categories and expenses.

## Auth Routes (same pattern as Day 89)
```python
@app.post("/register")
@app.post("/login")   # returns a JWT
```

## Category Routes
```python
@app.get("/categories")
@app.post("/categories")
```

## Expense Routes (the core feature)
```python
@app.get("/expenses")              # list current user's expenses
@app.post("/expenses")             # log a new expense
@app.patch("/expenses/{id}")       # edit an expense
@app.delete("/expenses/{id}")      # remove an expense
```

## Design Decisions
- Every expense route uses `Depends(get_current_user)` — users can only
  see/edit their **own** expenses (same ownership check pattern as the
  Task API on Day 89).
- `date` fields use Python's `datetime.date` type — FastAPI/Pydantic
  validate the format automatically from ISO strings like `"2026-08-14"`.
- Category creation is intentionally open to any logged-in user for
  simplicity; a production app might restrict this to admins.

## Validation with Pydantic
```python
class ExpenseIn(BaseModel):
    amount: float
    note: str | None = None
    date: date
    category_id: int

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("amount must be greater than 0")
        return v
```
Custom validators (`@field_validator`) let you enforce business rules
(like "amount must be positive") directly in the schema, so bad data
never reaches the database.

## Summary
This phase turns the data model into a working API — the same
routes-+-auth-+-database pattern from Day 89, now applied to the
capstone's expense-tracking domain, with an added custom validator for
extra data integrity.
