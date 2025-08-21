from pydantic import BaseModel, PrivateAttr
from typing import List, Dict
from fastapi import WebSocket
from typing import Any
from random import randint


class Session(BaseModel):
    session_id: int
    user_id: int
    _websocket: WebSocket = PrivateAttr()

    def send_message(self, message: Any):
        if self._websocket.client_state == WebSocket.CONNECTED:
            self._websocket.send_json(message)
        else:
            print(f"WebSocket is not connected for session {self.session_id}.")

    def get_connection(self) -> WebSocket:
        return Session(
            session_id=self.session_id,
            user_id=self.user_id,
            _websocket=self._websocket
        )
    
    def send_message(self, message: Any):
        if self._websocket.client_state == WebSocket.CONNECTED:
            self._websocket.send_json(message)
        else:
            print(f"WebSocket is not connected for session {self.session_id}.")


class SessionStorage(BaseModel):
    chat_rooms: Dict[int, List[Session]] = {}

    def add_connection(self, session: Session):
        chat_room_id = randint(1, 100)

        if chat_room_id not in self.chat_rooms: 
            self.chat_rooms[chat_room_id] = []
        self.chat_rooms[chat_room_id].append(session)

    def get_connection(self, session_id: str) -> WebSocket:
        chat_room = self.chat_rooms.get(session_id)
        if chat_room:
            return chat_room.get_connection()
        else:
            print(f"No session found for session_id: {session_id}")
            return None
        
    def broadcast_message(self, chat_room_id: int, message: Any):
        chat_room = self.chat_rooms.get(chat_room_id)

        for session in chat_room:
            session.send_message(message)

    

    

    
