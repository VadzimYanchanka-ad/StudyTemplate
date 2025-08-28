from fastapi import APIRouter

from . import root
from . import ws
from . import users
from . import messages
from . import chats


api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(ws.router)
api_router.include_router(users.router)
api_router.include_router(messages.router)
api_router.include_router(chats.router)

