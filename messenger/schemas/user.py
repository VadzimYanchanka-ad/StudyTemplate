from pydantic import BaseModel

class User(BaseModel):
    username: str
    first_name: str
    second_name: str
    last_name: str

class CreateUser(User):
    pass

class UserOut(User):
    username: str

    class Config:
        orm_mode = True