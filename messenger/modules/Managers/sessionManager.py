from fastapi import HTTPException
from uuid import UUID
from messenger.schemas.sessionStorage import SessionStorage, Session
from typing import List


class SessionManager:
    session_storage: SessionStorage = SessionStorage()

    def add_session(self, chat_room_id: UUID, session: Session):
        if chat_room_id not in self.session_storage:
            self.session_storage.chat_rooms[chat_room_id] = []
        self.session_storage.chat_rooms[chat_room_id].append(session)

    async def get_session(self, chat_room_id: int, session_id: int) -> Session:
        chat_room = self.session_storage.get(chat_room_id)
        if not chat_room:
            raise HTTPException(status_code=404, detail="Chat room not found")

        for session in chat_room:
            if session.session_id == session_id:
                return session

        raise HTTPException(status_code=404, detail="Session not found")

    async def get_chat_room(self, chat_room_id: int) -> List[Session]:
        chat_room = self.session_storage.get(chat_room_id)
        if chat_room:
            return chat_room
        else:
            raise HTTPException(status_code=404, detail="Chat room not found")
