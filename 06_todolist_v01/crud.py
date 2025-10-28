from models import Todo, User
from sqlalchemy.orm import Session


class TodoRepository:

    def __init__(self,session:Session):
        self.session=session

    def create_todo(self,todo:Todo)-> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    # def find_all_todos(self)->list[Todo]:
    #     pass
    def new_todo_by_user(self,user_id:int,todo:Todo)->Todo:
        user = self.session.get(User,user_id)
        user.todos.append(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    def get_todos_by_user(self,user_id:int)->list[Todo]:
        return self.session.query(Todo).filter(Todo.user_id== user_id).all()
    ################ später #########################
    #deleteById, update/updateState, findByTask,  findByState

class UserRepository:
    def __init__(self,session:Session):
        self.session=session
    def create_user(self,user:User)->User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    # def find_all_users(self)->list[User]:
    #     pass