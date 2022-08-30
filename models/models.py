from pydantic import BaseModel


class LoginUserModel(BaseModel):
    login: str
    password: str


class RegistrationUserModel(BaseModel):
    login: str
    password: str
