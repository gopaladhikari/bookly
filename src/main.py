from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.core.database import init_db
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse


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


@app.exception_handler(SQLAlchemyError)
async def database_error_handler(request, exc: SQLAlchemyError):

    print(f"CRITICAL DATABASE ERROR: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Our database is currently experiencing issues. Please try again later."
        },
    )


app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
