import re
from app.core.exceptions.authentication_exeptions import InvalidEmailFormateException, InvalidPasswordFormateException

from app.models.user_models import SignUp


def validate_email(email: str):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


def validate_password(password: str) -> str | bool:
    if len(password) < 8:
        raise InvalidPasswordFormateException("Password should be 8 characters")
    if not re.search(r'[A-Z]', password):
        raise InvalidPasswordFormateException("Password should contain least one uppercase character")
    if not re.search(r'[a-z]', password):
        raise InvalidPasswordFormateException("Password should contain least one lowercase character")
    if not re.search(r'[0-9]', password):
        raise InvalidPasswordFormateException("Password should contain least one number")
    if not re.search(r'[@$!%*?&#]', password):
        raise InvalidPasswordFormateException("Password should contain least one special character")

    return True


def signup_validation(user_details: SignUp) -> str | bool:
    if not validate_email(user_details.email):
        raise InvalidEmailFormateException(user_details.email)
    elif len(user_details.firstName) == 0:
        return "first name should not empty"
    elif len(user_details.lastName) == 0:
        return "last name should not empty"
    password_validation = validate_password(user_details.password)
    if type(password_validation) == str:
        return password_validation
    else:
        return True
