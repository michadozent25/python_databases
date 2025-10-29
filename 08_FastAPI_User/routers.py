from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from models import User
from database import Base, engine, get_db
from schemas import UserCreate, UserRead, UserUpdate
from crud import UserRepository


user_router = APIRouter() #user_router =APIRouter(), todo_router =APIRouter()


@user_router.post("/user/",response_model=UserRead)
def create_user(user:UserCreate,db:Session=Depends(get_db)): #Dependencyinjection
    repo =UserRepository(db)
    if repo.get_user_by_email(user.email):
        raise HTTPException(status_code=400,detail="Email already registered!")
    new_user = User(**user.model_dump())    #convert to ORM-User
    return repo.create_user(new_user)

