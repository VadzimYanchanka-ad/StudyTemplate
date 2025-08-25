from fastapi import APIRouter

from . import root
from . import ws


api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(ws.router)
