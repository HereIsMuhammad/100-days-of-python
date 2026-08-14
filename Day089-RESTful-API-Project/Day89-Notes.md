# Day 89: RESTful API Project

## Project: Task Management API
This project ties together Days 83-88: HTTP fundamentals, FastAPI routing,
REST conventions, JWT authentication, and SQLAlchemy database integration.

## Features
- User registration & login (JWT-based auth, from Day 86).
- Authenticated users can create, list, update, and delete their own tasks.
- Data persisted in SQLite via SQLAlchemy (Day 87-88).
- Proper status codes and error handling throughout.

## Endpoint Design
| Method | Path | Description | Auth required |
|---|---|---|---|
| POST | `/register` | Create a new user | No |
| POST | `/login` | Get a JWT access token | No |
| GET | `/tasks` | List current user's tasks | Yes |
| POST | `/tasks` | Create a task | Yes |
| PATCH | `/tasks/{id}` | Update a task (e.g. mark complete) | Yes |
| DELETE | `/tasks/{id}` | Delete a task | Yes |

## Design Notes
- Every task is linked to a `user_id` foreign key — users can only see and
  modify their **own** tasks (checked in each route).
- Passwords are hashed with `passlib`, never stored in plain text.
- `Depends(get_current_user)` protects task routes; `Depends(get_db)`
  injects a database session — combining two dependency patterns from
  earlier days.

## Running the Project
```bash
pip install fastapi "uvicorn[standard]" sqlalchemy python-jose[cryptography] passlib[bcrypt]
uvicorn Day89_TaskAPIProject:app --reload
```
Then visit `/docs` for the interactive Swagger UI to try every endpoint.

## Ideas to Extend
- Add task due-dates and priority levels.
- Add pagination to `GET /tasks`.
- Add refresh tokens for longer sessions.
- Write `pytest` tests for every endpoint (Day 79!).

## Summary
This is a complete, minimal-but-real backend API — the same architecture
pattern (routes → auth → database) used in production systems, just
scaled down for learning.
