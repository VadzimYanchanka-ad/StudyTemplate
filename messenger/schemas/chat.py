from pydantic import BaseModel

class Chat(BaseModel):
    name: str

class CreateChat(Chat):
    pass

class ChatOut(Chat):
    id: int

    class Config:
        orm_mode = True