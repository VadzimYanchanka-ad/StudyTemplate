from fastapi import APIRouter, WebSocket, status, HTTPException
from messenger.modules.Managers.events import eventManager
from messenger.schemas.sessionStorage import Session
import uuid
from messenger.modules.Managers.sessionManager import SessionManager


router = APIRouter()
session_manager = SessionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    
    sender_id = websocket.headers.get("sender_id")
    if not sender_id:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    
    session = Session(user_id=int(sender_id), websocket=websocket)
    chat_room_id = uuid.uuid4
    session_manager.add_session(chat_room_id, session)

    while True:
        data = await websocket.receive_json()
        event_name = data.get("event")

        await eventManager.handle_event(event_name, websocket, data)

