from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#postgresql+psycopg2://postgres:@localhost:5432/db_python05
engine = create_engine("mysql+pymysql://root:@localhost:3306/db_python07",echo=True)# mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATENBANK
Session = sessionmaker(bind=engine) # hier entsteht eine Klasse -type(...)
session = Session() # Session-Objekt wird erzeugt

Base = declarative_base()