# Standard Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine =  create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine) 
session = Session() # kapselt Datenbankzugriff -> kein direkter Zugriff auf Datenbank
Base = declarative_base()  # alle Model-Klassen erben von Base (Objekte für die Datenbank)
