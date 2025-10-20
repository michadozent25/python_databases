from sqlalchemy import Column, Integer, String
from database import Base

class User(Base): # alle Entity (DB)-Klassen erben von Base

    ''' Model-Klasse (Entity) - Datenbank-Konfiguration'''
    __tablename__="user"
    id=Column(Integer,primary_key=True)# default Auto-Increment
    name=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False,unique=True)

    def __repr__(self):
        return f"User(id={self.id},name={self.name},email={self.email})"