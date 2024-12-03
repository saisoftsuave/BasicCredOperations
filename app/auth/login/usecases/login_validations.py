import re



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
