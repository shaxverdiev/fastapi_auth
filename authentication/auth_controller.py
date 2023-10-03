from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.db import session



import models.auth_model as models
import schemas.auth_schemas as schemas


import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_user_db(response: Response, db: Session, user: schemas.UserToken): 
    db_user = models.UserModel(
        email=user.email, 
        password=get_hash_password(user.password),
        firstname=user.firstname,
        lastname=user.lastname,
        role=user.role,
        access_token=create_token(data={"sub":user.email})
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    response.set_cookie(key="access_token", value=db_user.access_token) 
    return "send access_token"


def login(response: Response, query_data: schemas.UserLogin, db: Session):
    user = get_user_by_email(db, query_data.email)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный логин или пароль")
    
    hashed_pswd_from_db = db.query(models.UserModel.password).filter(models.UserModel.email == query_data.email).first().password 
    if not verify_password(query_data.password, str(hashed_pswd_from_db)):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный логин или пароль")

    refresh_token = create_token(data={"sub": query_data.email}) 

    db.query(models.UserModel).filter(models.UserModel.email == query_data.email).update({models.UserModel.access_token: refresh_token}) 
    db.commit()
    
    response.set_cookie(key="access_token", value=refresh_token)
    return "success login and refresh token"


def get_user_by_email(db: session, email: str): 
    try:
        return db.query(models.UserModel).filter(models.UserModel.email == email).first()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не найден")


def create_token(data: dict, expires_delta: timedelta = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy() 
    expire = datetime.utcnow() + timedelta(minutes=10) 
    to_encode.update({"exp": expire})  
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  
    return encoded_jwt


def get_hash_password(password):
    hashing = pwd_context.hash(password)
    return hashing


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)  
    





