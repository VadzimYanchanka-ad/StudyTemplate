from fastapi import WebSocket
from messenger.schemas.sessionStorage import SessionStorage, Session
from pydantic import BaseModel


class SessionManager(BaseModel):
    sessionStorage: SessionStorage = SessionStorage()

    def add_session(self, user_id: int, session_id: int,  websocket: WebSocket):
        session = Session(
            session_id=session_id,
            user_id=user_id,
            _websocket=websocket
        )
        
        self.sessionStorage.add_connection(session)
    
    def get_session(self, session_id: int) -> WebSocket:
        return self.sessionStorage.get_connection(session_id)