from pydantic import BaseModel, PrivateAttr
from typing import List, Dict
from uuid import UUID
from fastapi import WebSocket


class Session(BaseModel):
    user_id: int
    _websocket: WebSocket = PrivateAttr()

class SessionStorage(BaseModel):
    chat_rooms: Dict[UUID, List[Session]] = {}