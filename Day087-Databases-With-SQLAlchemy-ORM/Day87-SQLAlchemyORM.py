"""
Day 87: Databases with SQLAlchemy ORM
Requires: pip install sqlalchemy
"""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User id={self.id} name={self.name!r}>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post id={self.id} title={self.title!r}>"


def main():
    engine = create_engine("sqlite:///day87_demo.db", echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Avoid duplicate demo data on repeat runs
    if not session.query(User).filter_by(email="ali@example.com").first():
        ali = User(name="Ali", email="ali@example.com")
        ali.posts.append(Post(title="Learning SQLAlchemy"))
        ali.posts.append(Post(title="Day 87 of #100DaysOfPython"))
        session.add(ali)
        session.commit()

    print("All users:")
    for user in session.query(User).all():
        print(" ", user)
        for post in user.posts:
            print("    -", post)

    session.close()


if __name__ == "__main__":
    main()
