from fastapi import APIRouter, Depends, status, HTTPException
from uuid import UUID
from src.core.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.dependencies import AccessTokenBearer
from src.auth.schema import TokenPayload
from .schema import ReviewSchema
from .service import ReviewService

review_router = APIRouter()

access_token_bearer = AccessTokenBearer()

review_service = ReviewService()


@review_router.post("/{book_id}")
async def create_review_by_book_id(
    book_id: UUID,
    review: ReviewSchema,
    token_details: TokenPayload = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    return review_service.create_review_by_book_id(
        token_details.sub, book_id, review, session
    )


@review_router.get("/{book_id}")
async def get_review_by_book_id(
    book_id: UUID,
    token_details: TokenPayload = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    return review_service.get_reviews_by_book_id(book_id, session)


@review_router.put("/{book_id}/{review_id}")
async def update_review_by_id(
    review_id: UUID,
    book_id: UUID,
    review: ReviewSchema,
    token_details: TokenPayload = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    return review_service.update_review_by_id(
        review_id, token_details.sub, book_id, review, session
    )


@review_router.delete("/{book_id}/{review_id}")
async def delete_review_by_id(
    review_id: UUID,
    book_id: UUID,
    token_details: TokenPayload = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    return review_service.delete_review_by_id(
        review_id, token_details.sub, book_id, session
    )
