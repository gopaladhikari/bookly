from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import BookWithId, BookCreate
from uuid import UUID
from sqlmodel import select, desc
from .models import Book


class BookService:
    async def get_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        books = await session.exec(statement)

        return books.all()

    async def get_book(self, book_id: UUID, session: AsyncSession):
        statement = select(Book).where(Book.id == book_id)

        book = await session.exec(statement)

        first_book = book.first()

        if first_book is None:
            return None

        return first_book

    async def create_book(self, book: BookCreate, session: AsyncSession):
        data = book.model_dump()

        new_book = Book(**data)

        session.add(new_book)

        await session.commit()

        await session.refresh(new_book)

        return new_book

    async def update_book(self, book: BookWithId, session: AsyncSession):
        book_to_update = await self.get_book(book.id, session)

        if book_to_update is None:
            return None

        data = book.model_dump()

        for key, value in data.items():
            setattr(book_to_update, key, value)

        await session.commit()

        await session.refresh(book_to_update)

        return book_to_update

    async def delete_book(self, book_id: UUID, session: AsyncSession):
        book_to_delete = await self.get_book(book_id, session)

        if book_to_delete is None:
            return None

        await session.delete(book_to_delete)

        await session.commit()

        return book_to_delete
