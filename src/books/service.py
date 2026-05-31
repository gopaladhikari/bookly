from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import Book, BookWithId
from uuid import UUID


class BookService:
    async def get_books(self, session: AsyncSession):
        return {"Hello": "World"}

    async def get_book(self, book_id: UUID, session: AsyncSession):
        return {"Hello": "World"}

    async def create_book(self, book: Book, session: AsyncSession):
        return {"Hello": "World"}

    async def update_book(self, book: BookWithId, session: AsyncSession):
        return {"Hello": "World"}

    async def delete_book(self, book_id: UUID, session: AsyncSession):
        return {"Hello": "World"}
