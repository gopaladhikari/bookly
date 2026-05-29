from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.core.database import init_db


# lifespan to run before and after the application starts and stops
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application...")
    await init_db()
    yield
    print("Stopping application...")


version = "v1"

app = FastAPI(
    title="Bookly API",
    description="A robust REST API service for book reviews.",
    version=version,
    lifespan=lifespan,
)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
