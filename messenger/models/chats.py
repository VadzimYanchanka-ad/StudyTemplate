from messenger.db.base import Base
from messenger.schemas.chat import CreateChat

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Chats(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

    messages = relationship("Messages", back_populates="chat")
    users = relationship("Users", secondary="chat_user", back_populates="chats")

    @classmethod
    def from_request(cls, new_chat: CreateChat):
        return cls(
            name = new_chat.name
            )