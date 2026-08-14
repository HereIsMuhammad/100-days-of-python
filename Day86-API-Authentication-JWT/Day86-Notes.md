# Day 86: API Authentication (JWT)

## Why Authentication?
Most real APIs need to know **who** is making a request before allowing
sensitive actions (viewing private data, deleting resources, etc.).

## What is a JWT?
JWT (JSON Web Token) is a compact, signed token containing claims
(data) about a user. Structure: `header.payload.signature`, each part
Base64-encoded. Because it's **signed** (not encrypted by default), the
server can verify it hasn't been tampered with, without a database lookup
on every request.

## Typical Auth Flow
1. User logs in with username/password.
2. Server verifies credentials, creates a JWT containing the user's identity.
3. Server sends the JWT back to the client.
4. Client includes it in the `Authorization: Bearer <token>` header on
   future requests.
5. Server verifies the token's signature and expiry on each request.

## Password Hashing
**Never** store plain-text passwords. Hash them with a strong algorithm.
```bash
pip install passlib[bcrypt]
```
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed = pwd_context.hash("mypassword")
pwd_context.verify("mypassword", hashed)  # True
```

## Creating & Verifying JWTs
```bash
pip install python-jose[cryptography]
```
```python
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "a-very-secret-key"
ALGORITHM = "HS256"

def create_token(data: dict, expires_minutes: int = 30):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
```

## Protecting FastAPI Routes
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        return payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.get("/profile")
def profile(user: str = Depends(get_current_user)):
    return {"user": user}
```

## Summary
JWT-based auth is stateless (no server-side session storage needed) and
widely used across REST APIs. Never store plain passwords — always hash
them, and keep your `SECRET_KEY` out of source control (use environment
variables).
