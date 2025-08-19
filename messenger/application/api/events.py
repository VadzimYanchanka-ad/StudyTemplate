from .eventHandler import event_manager
from fastapi import APIRouter, WebSocket
import time

class Message:
    def __init__(self, timestamp: str, content: str, sender_id: int, chat_id: int):
        self.timestamp = timestamp
        self.content = content
        self.sender_id = sener_id
        self.chat_id = chat_id

@event_manager.e
async def send_message(websocket: WebSocket, data: dict):
    msg = Message(
        timestamp=time.time(), 
        content=data.get("content"),
        sender_id=data.get("sender_id"),
        chat_id = data.get("chat_id"))
    
    await websocket.send_json(
        {
            "timestab": msg.timestamp,
            "content": msg.content,
            "sender_id": msg.sender_id,
            "chat_id": msg.chat_id
        }
    )