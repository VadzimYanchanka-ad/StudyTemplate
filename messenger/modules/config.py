import os
from typing import TypeVar

from dotenv import load_dotenv
from loguru import logger

dotenv_path = os.getenv("DOTENV_PATH")
if dotenv_path:
    assert os.path.exists(dotenv_path), f"Dotenv file not found at {dotenv_path}"
    logger.info(f"Loading environment variables from {dotenv_path}")

load_dotenv(dotenv_path)

T = TypeVar("T")


class Config:
    PORT: int = 8000

    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_DATABASE: str
    PG_SCHEMA: str
    IS_DB_ECHO_ENABLED: bool = False

    def __init__(self):
        self.PG_HOST = os.getenv("PG_HOST")
        self.PG_PORT = int(os.getenv("PG_PORT"))
        self.PG_USER = os.getenv("PG_USER")
        self.PG_PASSWORD = os.getenv("PG_PASSWORD")
        self.PG_DATABASE = os.getenv("PG_DATABASE")
        self.PG_SCHEMA = os.getenv("PG_SCHEMA")
        self.IS_DB_ECHO_ENABLED = os.getenv("IS_DB_ECHO_ENABLED", False)

    @property
    def PG_URL(self) -> str:
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DATABASE}"


config = Config()
