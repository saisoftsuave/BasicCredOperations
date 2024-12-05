import re

from app.models.user_models import SignUp


def validate_email(email : str) :
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


def validate_password(password: str) -> str | bool:
    if len(password) < 8:
        return "Password should be 8 characters"
    if not re.search(r'[A-Z]', password):
        return "Password should contain least one uppercase character"
    if not re.search(r'[a-z]', password):
        return "Password should contain least one lowercase character"
    if not re.search(r'[0-9]', password):
        return "Password should contain least one number"
    if not re.search(r'[@$!%*?&#]', password):
        return "Password should contain least one special character"

    return True

def signup_validation(user_details : SignUp) -> str | bool:
    password_validation = validate_password(user_details.password)
    if not validate_email(user_details.email):
        return "Invalid email formate"
    elif len(user_details.firstName) == 0:
        return "first name should not empty"
    elif len(user_details.lastName) == 0:
        return "last name should not empty"
    elif type(password_validation) == str:
        return password_validation
    else:
        return True

