"""
Day 97: Capstone Project — Architecture & Setup
Defines the database models and creates the tables for the
Personal Expense & Budget Tracker (the capstone project spanning
Days 97-100).
Requires: pip install sqlalchemy
"""

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///./capstone_expense_tracker.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    expenses = relationship("Expense", back_populates="owner")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    expenses = relationship("Expense", back_populates="category")


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    note = Column(String, nullable=True)
    date = Column(Date, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    owner = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")


def setup_database():
    Base.metadata.create_all(bind=engine)
    print(f"Database ready at: {DATABASE_URL}")
    print("Tables created:", list(Base.metadata.tables.keys()))


def seed_default_categories():
    """Add a few starter categories if they don't already exist."""
    db = SessionLocal()
    defaults = ["Food", "Rent", "Transport", "Entertainment", "Utilities"]
    for name in defaults:
        if not db.query(Category).filter_by(name=name).first():
            db.add(Category(name=name))
    db.commit()
    print("Seeded default categories:", defaults)
    db.close()


if __name__ == "__main__":
    setup_database()
    seed_default_categories()
