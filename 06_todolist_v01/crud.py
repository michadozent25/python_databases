from models import Todo, User

class TodoRepository:
    def create_todo(self,todo:Todo)-> Todo:
        pass
    def find_all_todos(self)->list[Todo]:
        pass

    ################ später #########################
    #deleteById, update/updateState, findByTask,  findByState

class UserRepository:
    def create_user(self,user:User)->User:
        pass
    def find_all_users(self)->list[User]:
        pass