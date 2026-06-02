from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from src.core.config import Config
from src.books.models import Book

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def init_db():
    async with engine.begin() as conn:

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():

    async with AsyncSessionLocal() as session:
        yield session
