import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from app.models import db_user_model
from app.jwt.jwt_authentication import encrypt_password
from app.models.user_models import User

DATABASE_URL = "postgresql://postgres:softsuave@localhost:5432/CrudOperations"
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://softsuave:softsuave@localhost:5431/usersdb")


engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()



