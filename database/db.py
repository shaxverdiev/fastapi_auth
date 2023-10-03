from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.getenv("GAS_DB_USERNAME")
passwd = os.getenv("GAS_DB_PASSWORD")
ip = os.getenv("GAS_DB_ADDRESS")
port = os.getenv("GAS_DB_PORT")
dbname = os.getenv("GAS_DB_NAME")

SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{passwd}@{ip}:{port}/{dbname}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal() 

Base = declarative_base()



