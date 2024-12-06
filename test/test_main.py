from fastapi import status
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.core.constants import FETCH_LIST_OF_USERS, AUTH_URL, BASE_URL, SIGNUP, LOGIN
from app.database import get_db, Base
from app.main import app
from test.testing_details import signup_request_valid_1, signup_request_invalid_1, signup_request_invalid_3, \
    login_valid_1

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

clint = TestClient(app)


def override_get_db():
    db = TestingSessionLocal()
    setup_db()
    try:
        yield db
    finally:
        db.close()
        teardown_db()


app.dependency_overrides[get_db] = override_get_db


def test_read_users():
    response = clint.get(AUTH_URL + FETCH_LIST_OF_USERS)
    assert response.status_code == status.HTTP_200_OK


def test_signup_user():
    response = clint.post(url=AUTH_URL + SIGNUP, json=signup_request_valid_1)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message": "registration successful! Please verify email",
        "user": f"${signup_request_valid_1.get("firstName") + signup_request_invalid_1.get("lastName")}"
    }


def test_signup_user_invalid_mail():
    response = clint.post(url=AUTH_URL + SIGNUP, json=signup_request_invalid_1)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_signup_user_invalid_password():
    response = clint.post(url=AUTH_URL + SIGNUP, json=signup_request_invalid_3)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_login_user():
    response = clint.post(url=AUTH_URL + LOGIN, json=login_valid_1)
    assert response.status_code == status.HTTP_200_OK

def setup_db():
    Base.metadata.create_all(bind=engine)


def teardown_db():
    Base.metadata.drop_all(bind=engine)
