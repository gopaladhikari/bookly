from fastapi import APIRouter, status, Depends, HTTPException
from src.core.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
from .schema import CreateBookSchema, UpdateBookSchema
from uuid import UUID
from typing import List
from .models import Book
from src.auth.dependencies import AdminChecker, TokenPayload

book_router = APIRouter()

book_service = BookService()

admin_checker = AdminChecker()


@book_router.get("/", response_model=List[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_books(session)

    return books


@book_router.get("/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def get_book(book_id: UUID, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_id, session)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(
    book: CreateBookSchema,
    session: AsyncSession = Depends(get_session),
    token_details: TokenPayload = Depends(admin_checker),
):
    user_id = token_details.sub
    new_book = await book_service.create_book(book, session, user_id)
    return new_book


@book_router.put("/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def update_book(
    book_id: UUID,
    book: UpdateBookSchema,
    session: AsyncSession = Depends(get_session),
    _: AdminChecker = Depends(admin_checker),
):
    updated_book = await book_service.update_book(book_id, book, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return updated_book


@book_router.delete(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    response_model=Book,
)
async def delete_book(
    book_id: UUID,
    session: AsyncSession = Depends(get_session),
    _: AdminChecker = Depends(admin_checker),
):
    deleted_book = await book_service.delete_book(book_id, session)

    if deleted_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return deleted_book
