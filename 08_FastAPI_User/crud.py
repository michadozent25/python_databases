from  sqlalchemy.orm import Session
from models import User

class UserRepository:

    def __init__(self, session:Session):
        self.session = session

    def create_user(self,user:User)->User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    def get_all_users(self)->list[User]:
        return self.session.query(User).all()
    
    def get_user_by_email(self,email:str)->User:
        return self.session.query(User).filter(User.email==email).first()
    def get_user_by_id(self,id:int)->User|None:
        return self.session.get(User,id)
    
    def delete_user(self,id:int)->bool:
        user = self.get_user_by_id(id)
        if(user):
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    def update_user(self, user_id:int,name:str,email:str)->User|None:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email =email
            self.session.commit()
            self.session.refresh(user)
        return user