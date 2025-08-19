from abc import abstractmethod, ABC
from fastapi import WebSocket, HTTPException, status


class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.events = {}

    def add_session(self, session_id: str, websocket: WebSocket):
        self.sessions[session_id] = websocket
    
    def get_session(self, session_id: str) -> WebSocket:
        return self.sessions.get(session_id)

    def event(self, event_name: str):
        def wrapper(func):
            self.events[event_name] = func()
            return func()
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




class EventHandler(ABC):
    @abstractmethod
    def handel_Event(self):
        pass
    
    @abstractmethod
    def store_connection(self, connection: WebSocket) -> HTTPException:
        pass

    @abstractmethod
    def remove_connection(self, connection: WebSocket) -> HTTPException:
        pass

class event_manager(EventHandler):
    active_connections: list[WebSocket] = []

    def __init__(self):
        self.active_connections = []

    def handel_Event(self, event: str) -> str: 
        return
    
    def store_connection(self, connection: WebSocket) -> HTTPException:
        if connection not in self.active_connections:
            self.active_connections.append(connection)
            return HTTPException(status_code=status.HTTP_200_OK, detail="Connection stored successfully")
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Connection already exists")
        
    def remove_connection(self, connection: WebSocket) -> HTTPException:
        if connection in self.active_connections:
            self.active_connections.remove(connection)
            return HTTPException(status_code=status.HTTP_200_OK, detail="Connection removed successfully")
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")