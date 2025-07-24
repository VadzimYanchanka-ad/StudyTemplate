from fastapi import APIRouter, Response
from pydantic import BaseModel, AfterValidator, ValidationError, field_validator, model_validator
from typing import Annotated
from enum import Enum
from messenger.schemas.users import UserStatus, User, UserResponse
import re



router = APIRouter()

users = []

id = 0



 

@router.get("/")
async def hello_world():
    return {"value": "Hello World"}

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



@router.post("/user")
async def create_user(user: User):
    try:
        global id
        user.id = id
        for u in users:
            if u.email == user.email:
                return {"message": "User with this email already exists"}
        users.append(user)
        id += 1
        return {"message": "User created"}
    except ValidationError:
        return {"message": "Incorrect password"}


@router.get("/user/{user_id}")
async def get_users(user_id: int):
    for u in users:
        if u.id == user_id:
            if u.status == UserStatus.active:
                usRe = UserResponse.create(u)
                return usRe
            if u.status == UserStatus.deleted or u.status == UserStatus.inactive:
                return Response(status_code=410)
            return Response(status_code=204)


@router.put("/user/{user_id}")
def update_user(user: User):
    for u in users:
        if u.id == user.id:
            u.status = user.status
            u.password = user.password
            return {"message": "User updated successfully", "user": u}
    return {"message": "User not found"}


@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            u.status = UserStatus.deleted
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}