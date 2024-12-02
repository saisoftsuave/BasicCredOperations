from typing import List

from models import User


def isExistingUser(listOfUsers : List[User], email : str) :
    for user in listOfUsers:
        if user.email == email:
            return True
    else:
        return False