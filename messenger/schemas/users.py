from enum import Enum
from pydantic import BaseModel, AfterValidator, ValidationError, field_validator
import re

class UserStatus(Enum):
    active = 1
    inactive = 2
    deleted = 3
    blocked = 4

class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    status: UserStatus = UserStatus.active
    password: str
    
    @field_validator("password", mode='before')
    @classmethod
    def check_password(cls, password: str):
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[^\w\s]', password))
        if len(password) < 8 or not has_digit or not has_symbol:
            raise ValidationError("Password must contain at least one digit")
        return password


class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    status: UserStatus

    @classmethod
    def create(cls, user: User):
        return cls(
            id=user.id,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            status=user.status
        )



