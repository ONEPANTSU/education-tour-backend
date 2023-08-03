from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.schemas import Response

tour_router = APIRouter(prefix="/tour", tags=["tour"])


@tour_router.get("/", response_model=Response)
async def get_all_events(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await get_all_tours_response(session=session)
