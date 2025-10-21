from models import User
from sqlalchemy.orm import Session
from sqlalchemy import text, select


def create_user(session:Session, user:User)->User:
    session.add(user)
    session.commit()
    session.refresh(user)
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

def update_user(session:Session,user:User) -> User|None:
    ''' User(id=1,email="max@web.de")'''
    db_user = session.get(User,user.id)
    if not db_user:
        return None
    # auch generisch möglich
    if user.name is not None:  
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    session.commit()
    session.refresh(db_user)
    return db_user
def get_users_by_name(session:Session, name:str)->list[User]:
    stmt = text("select * from user where name ilike :name")
    return session.execute(stmt, {"name":f"%{name}%"})

def get_users_by_name(session:Session, name:str)->list[User]:
    stmt = select(User).where(User.name.ilike(f"%{name}%"))
    return session.execute(stmt).scalars().all()