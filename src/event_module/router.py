from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.event_module.database.category.category_response_handler import (
    CategoryResponseHandler,
)
from src.event_module.database.event.event_response_handler import EventResponseHandler
from src.event_module.database.event_tag.event_tag_response_handler import (
    EventTagFilter,
    EventTagResponseHandler,
)
from src.event_module.database.tag.tag_response_handler import TagResponseHandler
from src.event_module.schemas import (
    CategoryCreate,
    CategoryUpdate,
    EventCreate,
    EventTagListCreate,
    EventTagListDelete,
    EventUpdate,
    TagCreate,
    TagUpdate,
)
from src.schemas import Response
from src.tour_module.database.tour_event.tour_event_responses import (
    TourEventResponseHandler,
)
from src.university_module.router import university_event_response_handler

event_router = APIRouter(prefix="/event", tags=["event"])
category_router = APIRouter(prefix="/event/category", tags=["category"])
tag_router = APIRouter(prefix="/event/tag", tags=["tag"])

event_response_handler = EventResponseHandler()
category_response_handler = CategoryResponseHandler()
tag_response_handler = TagResponseHandler()
event_tag_response_handler = EventTagResponseHandler()
tour_event_response_handler = TourEventResponseHandler()


@event_router.get("/", response_model=Response)
async def get_all_events(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await event_response_handler.get_all(session=session)


@event_router.get("/category_filter/", response_model=Response)
async def get_events_by_categories(
    category_list: list[int] = Query(),
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


@tag_router.get("/", response_model=Response)
async def get_all_tags(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await tag_response_handler.get_all(session=session)


@tag_router.get("/{tag_id}", response_model=Response)
async def get_tag_by_id(
    tag_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tag_response_handler.get_by_id(model_id=tag_id, session=session)


@tag_router.post("/", response_model=Response)
async def create_tag(
    tag: TagCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tag_response_handler.create(model_create=tag, session=session)


@tag_router.put("/{tag_id}", response_model=Response)
async def update_tag(
    tag: TagUpdate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tag_response_handler.update(model_update=tag, session=session)


@tag_router.delete("/{tag_id}", response_model=Response)
async def delete_tag(
    tag_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tag_response_handler.delete(model_id=tag_id, session=session)


@event_router.post("/{event_id}/set_tags", response_model=Response)
async def set_tags(
    event_tag: EventTagListCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_tag_response_handler.create_list(
        model_create=event_tag, session=session
    )


@event_router.get("/tour_filter/{tour_id}", response_model=Response)
async def get_event_id_list_by_tour_id(
    tour_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_event_response_handler.get_by_filter(
        value=tour_id, session=session
    )


@tag_router.get("/event_filter/{event_id}", response_model=Response)
async def get_tag_id_list_by_event_id(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_tag_response_handler.get_by_filter(
        event_tag_filter=EventTagFilter.EVENT, value=event_id, session=session
    )


@event_router.get("/tag_filter/{tag_id}", response_model=Response)
async def get_event_id_list_by_tag_id(
    tag_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_tag_response_handler.get_by_filter(
        event_tag_filter=EventTagFilter.TAG, value=tag_id, session=session
    )


@event_router.delete("/{event_id}/event_tag", response_model=Response)
async def delete_event_tag(
    event_tags: EventTagListDelete, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_tag_response_handler.delete_by_delete_schema(
        model_delete=event_tags, session=session
    )


@event_router.get("/university_filter/{university_id}", response_model=Response)
async def get_event_id_list_by_university_id(
    university_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_event_response_handler.get_by_filter(
        value=university_id, session=session
    )
