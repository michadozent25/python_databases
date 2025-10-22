from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base): # alle Entity (DB)-Klassen erben von Base

    ''' Model-Klasse (Entity) - Datenbank-Konfiguration'''
    __tablename__="user"
    id=Column(Integer,primary_key=True)# default Auto-Increment
    name=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False,unique=True)
    addresses = relationship("Address",back_populates="user",cascade="all")#bidirectional

    def __repr__(self):
        return f"User(id={self.id},name={self.name},email={self.email})"
class Address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True)# default Auto-Increment
    postal_code=Column(String(10),nullable=False)
    city=Column(String(100),nullable=False)
    street=Column(String(200),nullable=False)
    user_id=Column(Integer,ForeignKey("user.id",ondelete="CASCADE"))
    user= relationship("User",back_populates="addresses")#bidirectional