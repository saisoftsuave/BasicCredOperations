from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from app import db_user_model
from app.jwt.jwt_authentication import encrypt_password
from app.models import User

URL_DATABASE = "postgresql://postgres:softsuave@localhost:5432/CrudOperations"



engine = create_engine(URL_DATABASE)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


def create_user(userDetails : User, db: Session) :
    db_user = db_user_model.DbUser(
        id=userDetails.id,
        firstName=userDetails.firstName,
        lastName=userDetails.lastName,
        email=userDetails.email,
        password=encrypt_password(userDetails.password)
    )
    db.add(instance=db_user)
    db.commit()

def is_existing_user(id : str,db: Session) -> bool:
    return db.query(db_user_model.DbUser).filter(db_user_model.DbUser.id == id).first()



