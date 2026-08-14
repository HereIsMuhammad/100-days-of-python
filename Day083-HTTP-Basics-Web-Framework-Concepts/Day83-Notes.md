# Day 83: HTTP Basics & Web Framework Concepts

## What is HTTP?
HTTP (HyperText Transfer Protocol) is how clients (browsers, apps) and
servers communicate on the web. It's a **request/response** protocol.

## HTTP Methods
| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Replace existing data entirely |
| PATCH | Partially update existing data |
| DELETE | Remove data |

## Anatomy of a Request
```
GET /users/5 HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
Content-Type: application/json
```

## Anatomy of a Response
```
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 5, "name": "Ali"}
```

## Common Status Codes
| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

## What is a Web Framework?
A web framework handles routing (which URL maps to which function),
request parsing, and response building, so you don't write raw socket code.
Popular Python frameworks:
- **Flask** — minimal, flexible
- **Django** — batteries-included, full-stack
- **FastAPI** — modern, async, automatic docs, type-hint based (we'll use this)

## Why FastAPI?
- Built on type hints → automatic request validation.
- Automatic interactive API docs (Swagger UI) at `/docs`.
- Native `async`/`await` support (ties back to Day 77!).

## Summary
Understanding raw HTTP concepts (methods, status codes, headers) makes it
much easier to understand what frameworks like FastAPI are doing under
the hood.
