from http.client import HTTPException

from fastapi import FastAPI,HTTPException

from constants import users,signup,deleteUser,updateUser
from users import users as listOfUsers
from models import SignUp, User
from usecases.authentication import isExistingUser

app = FastAPI()

@app.get(users)
async def fetch_users() :
    return listOfUsers

@app.post(signup)
def user_signup(userDetails : SignUp) :
    if isExistingUser(listOfUsers,userDetails.email):
        return "You have an existing account!, Pleas login"
    else:
        listOfUsers.append(User(
            useName = userDetails.useName,
            firstName=userDetails.firstName,
            lastName=userDetails.lastName,
            email=userDetails.lastName,
            password=userDetails.password
        ))
        return "SignUp success"


@app.delete(deleteUser)
def delete_user(user_id : str):
    for user in listOfUsers:
        if user.useName == user_id :
            listOfUsers.remove(user)
            return "User Deleted successfully"
    else:
        raise HTTPException(
            status_code=404,
            detail="The user with this ID " + user_id + " not found"
        )


@app.put(updateUser)
def update_user(userDetails : User):
    for user in listOfUsers:
        if user.useName == userDetails.useName:
            if userDetails.firstName is not None :
                user.firstName = userDetails.firstName
            if userDetails.lastName is not None :
                user.lastName = userDetails.lastName
            if userDetails.firstName is not None :
                user.email = userDetails.email
            if userDetails.firstName is not None :
                user.password = userDetails.password
            return "user updated successfully"
    raise HTTPException(
        status_code=404,
        detail="The user not found"
    )