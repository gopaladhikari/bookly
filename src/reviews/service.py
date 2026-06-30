from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from uuid import UUID
from .schema import ReviewSchema
from .models import Review
from sqlmodel import select

book_service = BookService()


class ReviewService:
    async def create_review_by_book_id(
        self, user_id: UUID, book_id: UUID, review: ReviewSchema, session: AsyncSession
    ):
        book = await book_service.get_book(book_id, session)

        if book is None:
            return None

        new_review = Review.model_validate(
            review,
            update={"book_id": book_id, "user_id": user_id},
        )

        session.add(new_review)

        await session.commit()

        await session.refresh(new_review)

        return new_review

    async def get_reviews_by_book_id(self, book_id: UUID, session: AsyncSession):
        statement = select(Review).where(Review.book_id == book_id)

        reviews = await session.exec(statement)

        return reviews.all()

    async def delete_review_by_id(
        self, review_id: UUID, user_id: UUID, book_id: UUID, session: AsyncSession
    ):
        statement = select(Review).where(
            (Review.id == review_id)
            & (Review.user_id == user_id)
            & (Review.book_id == book_id)
        )

        review_dict = await session.exec(statement)

        review = review_dict.first()

        if review is None:
            return None

        await session.delete(review)

        await session.commit()

        return review

    async def update_review_by_id(
        self,
        review_id: UUID,
        user_id: UUID,
        book_id: UUID,
        review: ReviewSchema,
        session: AsyncSession,
    ):
        statement = select(Review).where(
            (Review.id == review_id)
            & (Review.user_id == user_id)
            & (Review.book_id == book_id)
        )

        existing_review_dict = await session.exec(statement)

        existing_review = existing_review_dict.first()

        if existing_review is None:
            raise ValueError("Review does not exist")

        updated_review = review.model_dump(exclude_unset=True)

        for key, value in updated_review.items():
            setattr(existing_review, key, value)

        session.add(existing_review)
        await session.commit()
        await session.refresh(existing_review)

        return existing_review
