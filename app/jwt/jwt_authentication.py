from datetime import timedelta, datetime

from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.util import deprecated

SECRET_KEY ="123FHKHSDFAFKHADOI239804"
HASHING_ALGORITH = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class Token(BaseModel):
    token : str
    type : str

def encrypt_password(password : str):
    return bcrypt_context.hash(password)

def verify_password(plain_password : str,encrypted_password : str) :
    return bcrypt_context.verify(plain_password,encrypted_password)

def create_jwt_token(email: str, expires: timedelta):
    expiration = datetime.utcnow() + expires
    data = {
        "email": email,
        "exp": expiration.timestamp()
    }
    return jwt.encode(data, SECRET_KEY, algorithm=HASHING_ALGORITH)


