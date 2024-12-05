import uuid

from pydantic import BaseModel


class User(BaseModel) :
    id : str
    firstName : str
    lastName : str
    email : str
    password : str



class SignUp(BaseModel) :
    id: str = uuid.uuid4()
    firstName: str
    lastName: str
    email: str
    password: str


