from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from .models import Tag
from uuid import UUID
from .schema import TagCreateModel
from typing import List

book_service = BookService()


class TagService:

    async def get_tags_from_book(self, session: AsyncSession, book_id: UUID):
        book = await book_service.get_book(book_id, session)

        if not book:
            raise ValueError("Book not found")

        return book.tags

    async def add_tag_to_book(
        self, session: AsyncSession, book_id: UUID, tags: List[TagCreateModel]
    ):

        book = await book_service.get_book(book_id, session)

        if book is None:
            raise ValueError("Book not found")

        for tag in tags:
            statement = select(Tag).where(Tag.title == tag.title)

            result = await session.exec(statement)

            existing_tag = result.first()

            if not existing_tag:
                existing_tag = Tag.model_validate(tag)

            if existing_tag not in book.tags:
                book.tags.append(existing_tag)

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book

    async def remove_tag_from_book(
        self, session: AsyncSession, book_id: UUID, tag_id: UUID
    ):
        book = await book_service.get_book(book_id, session)

        if book is None:
            raise ValueError("Book not found")

        statement = select(Tag).where(Tag.id == tag_id)

        tag = await session.exec(statement)

        tag = tag.first()

        if tag is None:
            raise ValueError("Tag not found")

        if tag in book.tags:
            book.tags.remove(tag)

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book
