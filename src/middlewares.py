from fastapi import FastAPI
from fastapi.requests import Request
import time
import logging

logger = logging.getLogger("uvicorn.access")

logging.disable = True


def register_middlewares(app: FastAPI):

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        message = f"{request.method} - {request.url.path} - {response.status_code} - {process_time:.4f}"

        print(message)

        return response
