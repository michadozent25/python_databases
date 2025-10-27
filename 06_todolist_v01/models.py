#TODO generic __repr__
from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Todo:
    __tablename__="todos"
    id=Column(Integer,primary_key=True)
    task=Column(String(100),nullable=False)
    description=Column(Text)
    deadline=Column(Date)
    state= Column(Enum("OPEN","IN_PROGRESS","DONE"),nullable=False,default="OPEN")
    #  user_id,  evtl. user

    

class User:
    __tablename__="users" 
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)
    password=Column(String(100),nullable=False) # FIXME Verschlüsselung