from sqlalchemy import Column, String, Boolean

from app.database import Base


class DbUser(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    firstName = Column(String, index=True)
    lastName = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    is_verified = Column(Boolean,index=True)