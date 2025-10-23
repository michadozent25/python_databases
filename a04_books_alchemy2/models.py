from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates,Mapped
from database import Base
import re


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(13), nullable=False, unique=True)
    title = Column(String(100), nullable=False)

    # 1 Buch → viele Autoren
    #authors = relationship("Author", back_populates="book", cascade="all, delete-orphan")
    authors: Mapped[list["Author"]] = relationship(
        back_populates="book", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}'), authors={len(self.authors)})"

    @staticmethod
    def _normalize_isbn(raw: str) -> str:
        """Entfernt Bindestriche und vereinheitlicht ISBN."""
        return re.sub(r"-", "", raw)

    @validates("isbn")
    def _validate_isbn(self, key, value):
        return Book._normalize_isbn(value)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    # Jeder Autor gehört zu genau einem Buch (FK auf books.id)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    book = relationship("Book", back_populates="authors")

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', book_id={self.book_id})"
