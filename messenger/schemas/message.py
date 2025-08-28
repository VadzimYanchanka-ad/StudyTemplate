from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class Message(BaseModel):   
    
    user_id: int
    chat_id: int
    message: str
    created_at: datetime | None = Field(default_factory=datetime.now)

    @field_validator("message")
    def check_content_length(cls, value: str):
        if len(value) > 500:
            raise ValueError("Content length exceeds 500 characters")
        return value
    
class MessageCreate(Message):
    pass

class MessageUpdate(BaseModel):
    message: str

class MessageOut(Message):
    message: str
    created_at: datetime

    class Config:
        orm_mode = True