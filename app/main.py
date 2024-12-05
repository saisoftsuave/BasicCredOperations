from http.client import HTTPException

from fastapi import FastAPI, HTTPException

from app.models import db_user_model
from app.auth.common.constants import DELETE_USER, UPDATE_USER, BASE_URL
from app.auth.routes.auth_routes import auth_router
from app.database import engine
from app.models.user_models import User
from users import users as listOfUsers

app = FastAPI(root_path=BASE_URL)

app.include_router(router=auth_router, tags=["auth"])


#db_user_model.Base.metadata.drop_all(bind=engine)

db_user_model.Base.metadata.create_all(bind=engine)


# @app.delete(DELETE_USER)
# def delete_user(user_id: str):
#     for user in listOfUsers:
#         if user.id == user_id:
#             listOfUsers.remove(user)
#             return "User Deleted successfully"
#     else:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this ID " + user_id + " not found"
#         )
#
#
# @app.put(UPDATE_USER)
# def update_user(userDetails: User):
#     for user in listOfUsers:
#         if user.id == userDetails.id:
#             if userDetails.firstName is not None:
#                 user.firstName = userDetails.firstName
#             if userDetails.lastName is not None:
#                 user.lastName = userDetails.lastName
#             if userDetails.firstName is not None:
#                 user.email = userDetails.email
#             if userDetails.firstName is not None:
#                 user.password = userDetails.password
#             return "user updated successfully"
#     raise HTTPException(
#         status_code=404,
#         detail="The user not found"
#     )
