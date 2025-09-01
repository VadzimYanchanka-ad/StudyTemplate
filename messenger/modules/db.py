from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from messenger.modules.config import config

class Database:
    def __init__(self):
        self.engine = create_async_engine(config.PG_URL)
        self.async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

    def get_session(self):
        return self.async_session_maker()
    
    def get_engine(self):
        return self.engine
    
async def get_db():
    db = data_base.get_session()
    try:
        yield db
    finally:
        await db.close()

data_base = Database()