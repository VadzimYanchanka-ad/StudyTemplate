from pydantic import BaseModel
from fastapi import WebSocket
from typing import Any


class EventManager(BaseModel):
    events: dict[str, Any] = {}

    def event(self, event_name: str) -> Any:
        def wrapper(func):
            self.events[event_name] = func
            return func
        return wrapper

    async def handle_event(self, event_name: str, websocket: WebSocket, data: dict):
        """
        event_name string like '/message/send'
        """
        handler = self.events.get(event_name)
        if handler:
            await handler(websocket, data)
        else:
            print(f"Нет обработчика события!")