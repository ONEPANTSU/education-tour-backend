from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.event_module.database.category.category_response_handler import (
    CategoryResponseHandler,
)
from src.event_module.database.event.event_response_handler import EventResponseHandler
from src.event_module.schemas import (
    CategoryCreate,
    CategoryUpdate,
    EventCreate,
    EventUpdate,
)
from src.schemas import Response

event_router = APIRouter(prefix="/event", tags=["event"])
category_router = APIRouter(prefix="/event/category", tags=["category"])

event_response_handler = EventResponseHandler()
category_response_handler = CategoryResponseHandler()


@event_router.get("/", response_model=Response)
async def get_all_events(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await event_response_handler.get_all(session=session)


@event_router.get("/category_filter/", response_model=Response)
async def get_events_by_categories(
    category_list: List[int] = Query(),
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await event_response_handler.get_by_categories(
        category_list=category_list, session=session
    )


@event_router.get("/category_filter/{category_id}", response_model=Response)
async def get_events_by_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.get_by_category(
        category_id=category_id, session=session
    )


@event_router.get("/{event_id}", response_model=Response)
async def get_event_by_id(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.get_by_id(model_id=event_id, session=session)


@event_router.post("/", response_model=Response)
async def create_event(
    event: EventCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.create(model_create=event, session=session)


@event_router.put("/{event_id}", response_model=Response)
async def update_event(
    event: EventUpdate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.update(model_update=event, session=session)


@event_router.delete("/{event_id}", response_model=Response)
async def delete_event(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.delete(model_id=event_id, session=session)


@category_router.get("/", response_model=Response)
async def get_all_categories(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await category_response_handler.get_all(session=session)


@category_router.get("/{category_id}", response_model=Response)
async def get_category_by_id(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await category_response_handler.get_by_id(
        model_id=category_id, session=session
    )


@category_router.post("/", response_model=Response)
async def create_category(
    category: CategoryCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await category_response_handler.create(
        model_create=category, session=session
    )


@category_router.put("/{category_id}", response_model=Response)
async def update_category(
    category: CategoryUpdate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await category_response_handler.update(
        model_update=category, session=session
    )


@category_router.delete("/{category_id}", response_model=Response)
async def delete_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await category_response_handler.delete(model_id=category_id, session=session)
