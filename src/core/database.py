from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from src.core.config import Config

import src.books.models

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
