import uuid

from pydantic import BaseModel


class User(BaseModel) :
    useName : str
    firstName : str
    lastName : str
    email : str
    password : str


class Login(BaseModel) :
    email : str
    password : str

class SignUp(BaseModel) :
    useName: str = uuid.uuid4()
    firstName: str
    lastName: str
    email: str
    password: str


