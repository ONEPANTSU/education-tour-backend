from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.event_module.schemas import (
    CategoryCreate,
    CategoryUpdate,
    EventCreate,
    EventUpdate,
)
from src.event_module.utils.category.responses import (
    create_category_response,
    delete_category_response,
    get_all_categories_response,
    get_category_by_id_response,
    update_category_response,
)
from src.event_module.utils.event.responses import (
    create_event_response,
    delete_event_response,
    get_all_events_response,
    get_event_by_id_response,
    get_events_by_category_response,
    update_event_response, get_events_by_categories_response,
)

event_router = APIRouter(prefix="/event", tags=["event"])
category_router = APIRouter(prefix="/event/category", tags=["category"])


@event_router.get("/")
async def get_all_events(session: AsyncSession = Depends(get_async_session)) -> dict:
    return await get_all_events_response(session=session)


@event_router.get("/category_filter/")
async def get_events_by_categories(
    category_list: List[int] = Query(), session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await get_events_by_categories_response(
        category_list=category_list, session=session
    )


@event_router.get("/category_filter/{category_id}")
async def get_events_by_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await get_events_by_category_response(
        category_id=category_id, session=session
    )


@event_router.get("/{event_id}")
async def get_event_by_id(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await get_event_by_id_response(event_id=event_id, session=session)


@event_router.post("/")
async def create_event(
    event: EventCreate, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await create_event_response(event=event, session=session)


@event_router.put("/{event_id}")
async def update_event(
    event: EventUpdate, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await update_event_response(event=event, session=session)


@event_router.delete("/{event_id}")
async def delete_event(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await delete_event_response(event_id=event_id, session=session)


@category_router.get("/")
async def get_all_categories(
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    return await get_all_categories_response(session=session)


@category_router.get("/{category_id}")
async def get_category_by_id(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await get_category_by_id_response(category_id=category_id, session=session)


@category_router.post("/")
async def create_category(
    category: CategoryCreate, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await create_category_response(category=category, session=session)


@category_router.put("/{category_id}")
async def update_category(
    category: CategoryUpdate, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await update_category_response(category=category, session=session)


@category_router.delete("/{category_id}")
async def delete_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> dict:
    return await delete_category_response(category_id=category_id, session=session)
