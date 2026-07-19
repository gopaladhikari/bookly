from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import TagSchema, TagCreateModel
from src.core.database import get_session
from src.auth.dependencies import AdminChecker, TokenPayload
from .services import TagService
from typing import List
from uuid import UUID

tags_router = APIRouter()

admin_checker = AdminChecker()

tag_service = TagService()


@tags_router.get("/book/{book_id}", response_model=List[TagSchema])
async def get_tags_from_book(
    book_id: UUID,
    _: TokenPayload = Depends(admin_checker),
    session: AsyncSession = Depends(get_session),
):
    try:
        tags = await tag_service.get_tags_from_book(session, book_id)

        return tags

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error getting tags from book: {e}",
        )


@tags_router.post("/book/{book_id}", response_model=List[TagSchema])
async def add_tag_to_book(
    book_id: UUID,
    tags: List[TagCreateModel],
    _: TokenPayload = Depends(admin_checker),
    session: AsyncSession = Depends(get_session),
):
    try:
        book = await tag_service.add_tag_to_book(session, book_id, tags)

        return book.tags

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error adding tag to book: {e}",
        )


@tags_router.delete("/book/{book_id}/tag/{tag_id}", response_model=List[TagSchema])
async def remove_tag_from_book(
    book_id: UUID,
    tag_id: UUID,
    _: TokenPayload = Depends(admin_checker),
    session: AsyncSession = Depends(get_session),
):
    try:
        book = await tag_service.remove_tag_from_book(session, book_id, tag_id)

        return book.tags

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error removing tag from book: {e}",
        )
