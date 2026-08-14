"""
Day 89: RESTful API Project — Task Management API
Combines FastAPI, JWT auth, and SQLAlchemy from Days 83-88.
Requires: pip install fastapi "uvicorn[standard]" sqlalchemy python-jose[cryptography] passlib[bcrypt]
Run with: uvicorn Day89_TaskAPIProject:app --reload
"""

from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, sessionmaker

# --- Config ---
SECRET_KEY = "day89-task-api-secret-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# --- Database setup ---
engine = create_engine("sqlite:///./day89_tasks.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    tasks = relationship("TaskModel", back_populates="owner")


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("UserModel", back_populates="tasks")


Base.metadata.create_all(bind=engine)

# --- Schemas ---
class UserIn(BaseModel):
    username: str
    password: str


class TaskIn(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


class TaskOut(BaseModel):
    id: int
    title: str
    completed: bool
    model_config = ConfigDict(from_attributes=True)


# --- Security helpers ---
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


# --- App ---
app = FastAPI(title="Day 89: Task Management API")


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


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(current_user: UserModel = Depends(get_current_user)):
    return current_user.tasks


@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(task: TaskIn, db: Session = Depends(get_db),
                 current_user: UserModel = Depends(get_current_user)):
    db_task = TaskModel(title=task.title, owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db),
                 current_user: UserModel = Depends(get_current_user)):
    task = db.query(TaskModel).filter_by(id=task_id, owner_id=current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if update.title is not None:
        task.title = update.title
    if update.completed is not None:
        task.completed = update.completed
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db),
                 current_user: UserModel = Depends(get_current_user)):
    task = db.query(TaskModel).filter_by(id=task_id, owner_id=current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
