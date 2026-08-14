# Day 87: Databases with SQLAlchemy ORM

## Why an ORM?
Day 66 used raw SQL with `sqlite3`. An ORM (Object-Relational Mapper) lets
you work with **Python classes and objects** instead of writing raw SQL —
SQLAlchemy translates your Python code into SQL behind the scenes.

## Setup
```bash
pip install sqlalchemy
```

## Defining a Model
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)   # creates the table if it doesn't exist
```

## Creating a Session
The session manages a "conversation" with the database.
```python
Session = sessionmaker(bind=engine)
session = Session()
```

## CRUD Operations
```python
# Create
new_user = User(name="Ali", email="ali@example.com")
session.add(new_user)
session.commit()

# Read
all_users = session.query(User).all()
one_user = session.query(User).filter_by(name="Ali").first()

# Update
one_user.email = "new_email@example.com"
session.commit()

# Delete
session.delete(one_user)
session.commit()
```

## Relationships (Foreign Keys)
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", backref="posts")
```
Now `user.posts` gives all posts by that user, and `post.author` gives the
User object.

## Summary
SQLAlchemy lets you define your database schema as Python classes and
query it with Python method calls instead of raw SQL strings — safer
(protects against SQL injection) and easier to maintain.
