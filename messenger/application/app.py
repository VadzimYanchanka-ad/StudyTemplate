from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from messenger.application.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def get_app() -> FastAPI:
    app = FastAPI(
        title="PMAgent API",
        description="API for PMAgent",
        version="1.0.0",
        openapi_url="/api/v1/openapi.json",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api/v1")

    return app
