from jose import JWTError, jwt
from fastapi import Request
from authentication.auth_controller import get_user_by_email
from fastapi import HTTPException, status
from database.db import session
from functools import wraps

import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ROLES = {"ADMIN":1, "MANAGER":5, "USER":10}


def auth_middleware(role: ROLES = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            try:
                token = request.headers["Authorization"][7:]
                user = decoded_bearer_token(token)
                role_check(user, role)
                return await func(request, *args, **kwargs)
            except JWTError:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизован")
        return wrapper
    return decorator


def decoded_bearer_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")
    f = get_user_by_email(db=session, email=email) # session
    return f
    

def role_check(user, role: ROLES = None):
    if int(user.role) <= role:
        return True
    else:
        raise HTTPException(status_code=409, detail="Недостаточно прав")
    





