"""
Day 88: FastAPI & Database Integration
Requires: pip install fastapi "uvicorn[standard]" sqlalchemy
Run with: uvicorn Day88_FastAPIWithDatabase:app --reload
"""

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# --- Database setup ---
DATABASE_URL = "sqlite:///./day88_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# --- SQLAlchemy model ---
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


Base.metadata.create_all(bind=engine)


# --- Pydantic schemas ---
class UserIn(BaseModel):
    name: str
    email: str


class UserOut(UserIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Day 88: FastAPI + SQLAlchemy")


@app.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    existing = db.query(UserModel).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
