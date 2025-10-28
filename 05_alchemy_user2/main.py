from database import Base, engine, session
from models import User,Address
import crud

def main():
    # #
    #Base.metadata.drop_all(engine)  -> see alembic
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    user = crud.create_user(session,User(name="Max",email="max@web.de"))
    
    crud.add_address(session,Address(postal_code="10244",city="Berlin",street="Teststr. 8"),user_id=user.id)
   
    print(user)

if __name__=="__main__":
    main()

