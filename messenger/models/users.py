from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from typing import List

from datetime import datetime

from messenger.db.base import Base
from messenger.schemas.user import CreateUser

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)

    messages = relationship("Messages", back_populates="user")
    chats = relationship("Chats", secondary="chat_user", back_populates="users")

    @classmethod
    def from_request(cls, new_user: CreateUser):
        return cls(
            username = new_user.username,
            first_name = new_user.first_name,
            second_name = new_user.second_name,
            last_name = new_user.last_name,
        )
