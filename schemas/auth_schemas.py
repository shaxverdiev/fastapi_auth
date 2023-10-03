from pydantic import BaseModel


class User(BaseModel):
    email: str  
    firstname: str | None = None
    lastname: str | None = None
    password: str
    role: str = "10"
    

class UserToken(User):
    access_token: str


class UserLogin(BaseModel):
    email: str
    password: str