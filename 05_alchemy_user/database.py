from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



engine = create_engine("mysql+pymysql://root:@localhost:3306/db_python04",echo=True)# mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATENBANK
Session = sessionmaker(bind=engine) # hier entsteht eine Klasse
session = Session() # Session-Objekt wird erzeugt

Base = declarative_base()