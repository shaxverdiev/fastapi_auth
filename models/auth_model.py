from sqlalchemy import Column, Integer, String

from database.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    role = Column(Integer, default=10)
    access_token = Column(String, unique=True)

