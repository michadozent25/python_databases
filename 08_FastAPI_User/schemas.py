from pydantic import BaseModel, EmailStr, Field
# Schema für REST /Routes
class UserBase(BaseModel):
    pass #hier default attributes

class UserCreate(BaseModel):
    name:str= Field(min_length=2,max_length=20)
    email:EmailStr


class UserRead(BaseModel):
    id:int
    name:str
    email:EmailStr
    class Config:# see reference
        from_attributes=True # ORM-Modelle kompatible machen


class UserUpdate(BaseModel):
    name:str= Field(min_length=2,max_length=20)
    email:EmailStr
