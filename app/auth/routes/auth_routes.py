from datetime import timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.common.constants import FETCH_LIST_OF_USERS, AUTH_URL, SIGNUP, LOGIN
from app.auth.login.models.login_model import Login
from app.auth.login.usecases.login_validations import validate_email, validate_password
from app.database import get_db, create_user, is_existing_user
from app.db_user_model import DbUser
from app.jwt.jwt_authentication import verify_password, create_jwt_token
from app.models import SignUp

auth_router = APIRouter(prefix=AUTH_URL)


@auth_router.get(FETCH_LIST_OF_USERS)
async def fetch_users(db: Session = Depends(get_db)):
    users = db.query(DbUser).all()
    return users


@auth_router.post(SIGNUP)
def user_signup(userDetails: SignUp, db: Session = Depends(get_db)):
    if not validate_email(userDetails.email):
        return "Invalid email formate"
    password_validation = validate_password(userDetails.password)
    if type(password_validation) == str:
        return password_validation
    if is_existing_user(userDetails.email, db):
        return "You have an existing account!, Please LOGIN"
    if len(userDetails.firstName) == 0:
        return "first name should not empty"
    if len(userDetails.lastName) == 0:
        return "last name should not empty"
    else:
        create_user(userDetails, db)
        return "SignUp success"


@auth_router.post(LOGIN)
def user_login(login: Login, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.email == login.email).first()
    if not user:
        return "Invalid login credentials"
    if not verify_password(login.password, user.password):
        return "Invalid Password"
    token = create_jwt_token(login.email,timedelta(minutes=10))
    user.jwt_token = token
    db.commit()
    return {
        "Status": "success",
        "token": token
    }
