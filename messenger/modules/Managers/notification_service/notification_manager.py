from pydantic import BaseModel
from collections.abc import Callable
from fastapi import HTTPException, status

class NotificationManager:
    notify_storage: dict[str, Callable[[str], Callable]] = {}

    def notify(self, notify_type: str) -> Callable:
        def wrapper(func):
            self.notify_storage[notify_type] = func
            return func
        return wrapper
    
async def handel_notify(self, notify_name: str, data: dict):
    handler = self.notify_storage.get(notify_name)
    if handler:
        await handler(data)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No handler for event: {notify_name}")