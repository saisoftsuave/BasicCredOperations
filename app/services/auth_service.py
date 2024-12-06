from sqlalchemy.orm import Session

from app.core.exceptions.authentication_exeptions import DatabaseOperationException
from app.core.jwt.jwt_authentication import encrypt_password
from app.models import db_user_model
from app.models.user_models import User


def create_user(userDetails: User, db: Session):
    try:
        db_user = db_user_model.DbUser(
            id=userDetails.id,
            firstName=userDetails.firstName,
            lastName=userDetails.lastName,
            email=userDetails.email,
            password=encrypt_password(userDetails.password),
            is_verified = False
        )
        db.add(instance=db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as error:
        raise DatabaseOperationException()


def is_existing_user(email: str, db: Session) -> bool:
    return db.query(db_user_model.DbUser).filter(db_user_model.DbUser.email == email).first()
