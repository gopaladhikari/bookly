from fastapi import APIRouter, status

book_router = APIRouter()


@book_router.get("/")
async def get_books():
    return {"Hello": "World"}
