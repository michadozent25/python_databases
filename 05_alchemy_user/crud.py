from models import User
from sqlalchemy.orm import Session


def create_user(session:Session, user:User)->User:
    session.add(user)
    session.commit()
    return user

def get_all_users(session:Session)-> list[User]:
    return session.query(User).all()

def get_user_by_id(session:Session,user_id:int)->User:
    return session.query(User).filter(User.id==user_id).first()# .filter(...).filter(...)


def delete_user_by_id(session:Session,user_id:int)->User:
    user = session.query(User).filter(User.id==user_id).first()
    if user:
        session.delete(user)
        session.commit()
    return user
def get_user_by_name(session:Session,name:str)->list[User]:
    return session.query(User).filter(User.name.ilike(f"%{name}%")).all() # Otto -> tt

def user_exists(session:Session,email:str)->bool:
    return session.query(User).filter(User.email==email).count()==1