from sqlalchemy import Column, Integer, String
from database import Base
import re
from sqlalchemy.orm import validates


class Book(Base):
    __tablename__="books"

    id=Column(Integer,primary_key=True)# default Auto-Increment
    isbn=Column(String(13),nullable=False)
    title=Column(String(100),nullable=False)
    author=Column(String(100),nullable=False)
    def __repr__(self):
        return f"User(id={self.id},name={self.isbn},email={self.title},,email={self.author})"
      
    @staticmethod
    def _normalize_isbn(raw:str):
        return re.sub(r"-","",raw)
    

    @validates("isbn")
    def _validate_isbn(self,key,value):
        return Book._normalize_isbn(value)
