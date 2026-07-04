from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from .schema import TagSchema
from src.core.database import get_session
from src.auth.dependencies import AdminChecker, TokenPayload
from .services import TagService
from typing import List

tags_router = APIRouter()

admin_checker = AdminChecker()

tag_service = TagService()


@tags_router.get("/", response_model=List[TagSchema])
async def get_tags(
    admin_checker: TokenPayload = Depends(admin_checker),
    session: AsyncSession = Depends(get_session),
):
    pass
