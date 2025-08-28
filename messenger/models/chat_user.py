from messenger.db.base import Base
from messenger.models.chats import Chats
from messenger.models.users import Users

from typing import List

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class ChatUser(Base):
    __tablename__ = "chat_user"

    chat_id: Mapped[List[Chats]] = mapped_column(ForeignKey("chats.id"), primary_key=True, nullable=False)
    user_id: Mapped[List[Users]] = mapped_column(ForeignKey("users.id"), primary_key=True, nullable=False)
