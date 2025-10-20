from database import Base, engine, session
from models import User
import crud

def main():
    # #
    #Base.metadata.drop_all(engine)  -> see alembic
    Base.metadata.create_all(engine)
    user = crud.create_user(session,User(name="Max",email="max@web.de"))
    print(user)

if __name__=="__main__":
    main()

