from fastapi import status
from starlette.testclient import TestClient

from app.auth.common.constants import FETCH_LIST_OF_USERS, AUTH_URL
from app.main import app


clint = TestClient(app)

#test db
db = {}


def test_read_users() :
    response = clint.get(AUTH_URL + FETCH_LIST_OF_USERS)
    assert response.status_code == status.HTTP_200_OK



