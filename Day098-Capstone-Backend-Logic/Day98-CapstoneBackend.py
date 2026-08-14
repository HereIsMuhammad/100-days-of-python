"""
Day 98: Capstone Project — Backend & Logic
Full FastAPI backend for the Expense Tracker (builds on Day 97's models).
Requires: pip install fastapi "uvicorn[standard]" sqlalchemy python-jose[cryptography] passlib[bcrypt]
Run with: uvicorn Day98_CapstoneBackend:app --reload
"""

from datetime import date, datetime, timedelta, timezone

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, ConfigDict, field_validator
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker

SECRET_KEY = "day98-capstone-secret-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

engine = create_engine("sqlite:///./capstone_expense_tracker.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    expenses = relationship("ExpenseModel", back_populates="owner")


class CategoryModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    expenses = relationship("ExpenseModel", back_populates="category")


class ExpenseModel(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    note = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    owner = relationship("UserModel", back_populates="expenses")
    category = relationship("CategoryModel", back_populates="expenses")


Base.metadata.create_all(bind=engine)


class UserIn(BaseModel):
    username: str
    password: str


class CategoryIn(BaseModel):
    name: str


class CategoryOut(CategoryIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


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


class ExpenseOut(BaseModel):
    id: int
    amount: float
    note: str | None
    date: date
    category_id: int
    model_config = ConfigDict(from_attributes=True)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise error
    except JWTError:
        raise error
    user = db.query(UserModel).filter_by(username=username).first()
    if user is None:
        raise error
    return user


app = FastAPI(title="Day 98: Expense Tracker Backend")


@app.post("/register", status_code=201)
def register(user: UserIn, db: Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    db_user = UserModel(username=user.username, hashed_password=pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    return {"message": "User registered successfully"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(username=form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()


@app.post("/categories", response_model=CategoryOut, status_code=201)
def create_category(category: CategoryIn, db: Session = Depends(get_db),
                     current_user: UserModel = Depends(get_current_user)):
    if db.query(CategoryModel).filter_by(name=category.name).first():
        raise HTTPException(status_code=400, detail="Category already exists")
    db_category = CategoryModel(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/expenses", response_model=list[ExpenseOut])
def list_expenses(current_user: UserModel = Depends(get_current_user)):
    return current_user.expenses


@app.post("/expenses", response_model=ExpenseOut, status_code=201)
def create_expense(expense: ExpenseIn, db: Session = Depends(get_db),
                    current_user: UserModel = Depends(get_current_user)):
    category = db.query(CategoryModel).get(expense.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_expense = ExpenseModel(**expense.model_dump(), owner_id=current_user.id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@app.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: int, db: Session = Depends(get_db),
                    current_user: UserModel = Depends(get_current_user)):
    expense = db.query(ExpenseModel).filter_by(id=expense_id, owner_id=current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
