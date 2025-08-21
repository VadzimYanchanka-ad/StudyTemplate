from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class Message(BaseModel):   
    timestamp: datetime | None = Field(default_factory=datetime.now)
    content: str
    sender_id: int
    chat_id: int


    @field_validator("content")
    def check_content_length(cls, value: str):
        if len(value) > 500:
            raise ValueError("Content length exceeds 500 characters")
        return value

