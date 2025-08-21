from messenger.modules.Managers.eventManager import EventManager
from messenger.modules.Managers.sessionManager import SessionManager
from fastapi import WebSocket
from fastapi.encoders import jsonable_encoder
from messenger.schemas.message import Message

eventManager = EventManager()

@eventManager.event("/message/send")
async def send_message(websocket: WebSocket, data: dict):
    msg = Message(
        content=data.get("content"),
        sender_id=data.get("sender_id"),
        chat_id = data.get("chat_id")
    )
    await websocket.send_json(jsonable_encoder(msg))
