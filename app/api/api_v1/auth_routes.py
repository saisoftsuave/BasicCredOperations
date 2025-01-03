from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.constants import FETCH_LIST_OF_USERS, AUTH_URL, SIGNUP, LOGIN, DELETE_USER, VERIFY_EMAIL, FORGET_PASSWORD
from app.models.login_model import Login
from app.models.request_models import ForgetPasswordRequestModel
from app.services.login_validations import signup_validation
from app.core.email_service import request_verification
from app.database import get_db
from app.core.exceptions.authentication_exeptions import UserExistedException, DatabaseOperationException
from app.models.db_user_model import DbUser
from app.core.jwt.jwt_authentication import verify_password, create_jwt_token, get_uuid_from_jwt, encrypt_password
from app.models.user_models import SignUp
from app.services.auth_service import create_user, is_existing_user

auth_router = APIRouter(prefix=AUTH_URL)


@auth_router.get(FETCH_LIST_OF_USERS)
async def fetch_users(db: Session = Depends(get_db)):
    users = db.query(DbUser).all()
    return users


@auth_router.post(SIGNUP)
def user_signup(userDetails: SignUp, db: Session = Depends(get_db)):
    validate_signup_details = signup_validation(userDetails)
    if type(validate_signup_details) == str:
        return validate_signup_details
    elif is_existing_user(userDetails.email, db):
        raise UserExistedException(payload="You have an existing account!, Please LOGIN")
    else:
        create_user(userDetails, db)
        token = create_jwt_token(userDetails.id, timedelta(minutes=10))
        request_verification(userDetails.email, token)
        return {
            "message": "registration successful! Please verify email",
            "user": f"${userDetails.firstName + userDetails.lastName}"
        }


@auth_router.post(LOGIN)
def user_login(login: Login, db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.email == login.email).first()
    if not user:
        return "Invalid login credentials"
    if not verify_password(login.password, user.password):
        return "Invalid Password"
    token = create_jwt_token(user.id, timedelta(minutes=10))
    if not user.is_verified:
        request_verification(email=login.email, token=token)
        return {
            "message": "Email sent to your mail please verify and try login"
        }
    return {
        "Status": "success",
        "token": token
    }


@auth_router.delete(DELETE_USER)
def delete_user(token: str, db: Session = Depends(get_db)):
    uuid = get_uuid_from_jwt(token)
    print(uuid)
    try:
        db_user = db.query(DbUser).filter(DbUser.id == uuid).first()
        db.delete(db_user)
        db.commit()
        return "user deleted successfully"
    except:
        raise DatabaseOperationException()


@auth_router.get(VERIFY_EMAIL)
def verify_email(token: str, db: Session = Depends(get_db)):
    uuid = get_uuid_from_jwt(token)
    try:
        db_user = db.query(DbUser).filter(DbUser.id == uuid).first()
        db_user.is_verified = True
        db.commit()
        return "user verified successfully"
    except:
        raise DatabaseOperationException()


@auth_router.put(FORGET_PASSWORD)
def forget_password(request: ForgetPasswordRequestModel, db: Session = Depends(get_db)):
    uuid = get_uuid_from_jwt(request.token)
    user = db.query(DbUser).filter(DbUser.id == uuid).first()
    is_valid_password = verify_password(request.previous_password, user.password)
    if is_valid_password:
        try:
            db_user = db.query(DbUser).filter(DbUser.id == uuid).first()
            db_user.password = encrypt_password(request.new_password)
            db.commit()
            return "Password changed successfully"
        except:
            raise DatabaseOperationException()
    else:
        raise HTTPException(status_code=404, detail={
            "message": "previous password was wrong"
        })
