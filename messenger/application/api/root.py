from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from eventHandler import SessionManager
from .events import send_message


router = APIRouter()
test_sender_id = 1

@router.get("/")
def hello_world():
    return {"value": "Hello World"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    session_manager = SessionManager()

    await websocket.accept()
    session_manager.add_session(test_sender_id, websocket)

    while True:
        data = await websocket.receive_json()
        event_name = data.get("event")

        await session_manager.handle_event(event_name, websocket, data)