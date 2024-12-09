from pydantic import BaseModel


class ForgetPasswordRequestModel(BaseModel):
    token: str
    previous_password: str
    new_password: str
