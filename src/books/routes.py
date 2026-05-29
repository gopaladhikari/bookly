from fastapi import APIRouter, status

book_router = APIRouter()


@book_router.get("/")
def get_books():
    return {"Hello": "World"}
