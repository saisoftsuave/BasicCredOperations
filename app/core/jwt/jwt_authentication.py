import os
from datetime import timedelta, datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.core.exceptions.authentication_exeptions import TokenValidationException

SECRET_KEY = os.getenv('SECRET_KEY',"1234567890492843haksdh8yqnwer")
HASHING_ALGORITH = os.getenv('HASHING_ALGORITH',"HS256")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_barrier = OAuth2PasswordBearer("auth/token")


class Token(BaseModel):
    access_token: str
    type_type: str


def encrypt_password(password: str):
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, encrypted_password: str):
    return bcrypt_context.verify(plain_password, encrypted_password)


def create_jwt_token(id: str, expires: timedelta):
    expiration = datetime.utcnow() + expires
    data = {
        "id": id,
        "exp": expiration
    }
    return jwt.encode(data, SECRET_KEY, algorithm=HASHING_ALGORITH)

def get_uuid_from_jwt(token : str):
    payload = jwt.decode(token,SECRET_KEY,algorithms=HASHING_ALGORITH)
    print(token)
    uuid = payload.get("id")
    if uuid is None:
        raise TokenValidationException()
    return uuid