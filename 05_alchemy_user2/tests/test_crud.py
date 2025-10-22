import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#------------
from models import User,Base
from crud import create_user, update_user

DATABASE_URL ="sqlite:///:memory:"
#DATABASE_URL="mysql+pymysql://root:@localhost:3306/db_python04"

@pytest.fixture
def session():# TODO Parameter
    engine = create_engine(DATABASE_URL, echo=False) # create if not exists - ORM-Klassen
    Base.metadata.create_all(engine)#alle Tabellen erzeugen
    TestSession = sessionmaker(bind=engine,autoflush=False)
    session = TestSession()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose() # DB-Verbindung beenden

def test_update_user_success(session): # def session()
    # Arrange
    u = User(name="Max",email="max@web.de")
    u  = create_user(session,u)
    assert u.id is not None
    # Act
    updated = update_user(session,User(id=u.id,name="Maximilian",email="maxi@web.de"))
    assert updated is not None
    assert updated.id == u.id
    assert updated.name =="Maximilian"
    assert updated.email == "maxi@web.de"

    # nochmal aus DB laden
    reloaded = session.get(User,u.id)
    assert reloaded.name == "Maximilian"
    assert reloaded.email == "maxi@web.de" 
## negativ Test
def test_update_user_not_found(session): # -> None
    updated = update_user(session,User(id=9999,name="Ghost",email="ghost@ghost.de"))
    assert updated is None
    reloaded = session.get(User,9999)
    assert reloaded is None