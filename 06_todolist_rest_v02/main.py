from datetime import date
from database import Base, engine, session
from models import User, Todo
from crud import UserRepository, TodoRepository

def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    user_repo = UserRepository(session)
    todo_repo = TodoRepository(session)

    u1 = User(name="Max",password="1234")
    create_user1 = user_repo.create_user(u1)
    print(create_user1)
    #todo_t1 = Todo(task="sport",description="laufen",deadline=date(2025,7,4),state="OPEN",user_id=create_user1.id)
    todo_t1 = Todo(task="sport",description="laufen",deadline=date(2025,7,4),state="OPEN")
    todo_repo.new_todo_by_user(create_user1.id,todo_t1)

    todo_t2 = Todo(task="einkaufen",description="Brot",deadline=date(2025,7,4),state="OPEN",user_id=create_user1.id)
    todo_repo.create_todo(todo_t2)


if __name__=="__main__":
    main()