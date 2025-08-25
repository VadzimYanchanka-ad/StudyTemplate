from pydantic import BaseModel
from fastapi import WebSocket, status, HTTPException
from typing import Any
from collections.abc import Callable


class EventManager(BaseModel):
    events: dict[str, Callable[[str], Callable]] = {}

    def event(self, event_name: str) -> Callable:
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
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No handler for event: {event_name}")