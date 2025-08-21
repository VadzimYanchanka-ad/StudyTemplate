from fastapi import APIRouter, WebSocket
from messenger.modules.Managers.events import eventManager
from messenger.modules.Managers.sessionManager import SessionManager


router = APIRouter()
sessionManager = SessionManager()

test_session_id = 1
test_sender_id = 1

@router.get("/")
def hello_world():
    return {"value": "Hello World"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    sessionManager.add_session(test_session_id, test_sender_id, websocket)

    while True:
        data = await websocket.receive_json()
        event_name = data.get("event")

        await eventManager.handle_event(event_name, websocket, data)