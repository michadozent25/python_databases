from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from typing import Generator
#FIXME Klasse/Methode
DATABASE_URL ="sqlite:///todolist.db"
engine = create_engine(DATABASE_URL,echo=True)# mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATENBANK



SessionLocal = sessionmaker(bind=engine) # hier entsteht eine Klasse -type(...)
Base = declarative_base()

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()