from fastapi import APIRouter, Response
# from authentication.auth_middleware_module import auth_middleware, ROLES
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse


import models.auth_model as models
import schemas.auth_schemas as  schemas
import authentication.auth_controller as auth_contrl
from dependency.dependendy_db import get_db 


router = APIRouter()


@router.post("/register")
async def create_user(response: Response, query_data: schemas.User, db: Session = Depends(get_db)):
    db_user = auth_contrl.get_user_by_email(db, email=query_data.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth_contrl.create_user_db(response, db=db, user=query_data)


@router.post("/signin")
async def signin(response: Response, query_data: schemas.UserLogin, db: Session = Depends(get_db)):
    to_login = auth_contrl.login(response, query_data, db=db)
    return to_login


@router.get("/my_friends")
# @auth_middleware(role=ROLES["ADMIN"])
async def get_my_friends():
        return "у тебя нет друзей"


#куки удаляются когда статика раздается с того же домена что и бэкенд
@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return "cookie is delete"


