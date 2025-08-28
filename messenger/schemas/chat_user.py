from pydantic import BaseModel

class ChatUserOut(BaseModel):
    chat_id: int
    user_id: int

    class Config:
        orm_mode = True