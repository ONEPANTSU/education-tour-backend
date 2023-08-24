from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.event_module.database.category.category_response_handler import (
    CategoryResponseHandler,
)
from src.event_module.database.event.event_response_handler import EventResponseHandler
from src.event_module.database.event_tag.event_tag_response_handler import (
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
from src.event_module.utils import check_university_event
from src.schemas import Response
from src.tour_module.database.tour_event.tour_event_responses import (
    TourEventResponseHandler,
)
from src.user_module.database.user_event.user_event_models import UserEventFilter
from src.user_module.router import user_event_response_handler
from src.utils import Role, access_denied, role_access

event_router = APIRouter(prefix="/event", tags=["event"])
category_router = APIRouter(prefix="/category", tags=["category"])
tag_router = APIRouter(prefix="/tag", tags=["tag"])

event_response_handler = EventResponseHandler()
category_response_handler = CategoryResponseHandler()
tag_response_handler = TagResponseHandler()
event_tag_response_handler = EventTagResponseHandler()
tour_event_response_handler = TourEventResponseHandler()


@event_router.get("/", response_model=Response)
async def get_events(
    category_list: Annotated[list[int] | None, Query()] = None,
    tag_id: Annotated[int | None, Query()] = None,
    tour_id: Annotated[int | None, Query()] = None,
    university_id: Annotated[int | None, Query()] = None,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await event_response_handler.get_by_filter(
        category_list=category_list,
        tag_id=tag_id,
        tour_id=tour_id,
        university_id=university_id,
        session=session,
    )


@event_router.get("/{event_id}", response_model=Response)
async def get_event_by_id(
    event_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await event_response_handler.get_by_id(model_id=event_id, session=session)


@event_router.post("/", response_model=Response)
async def create_event(
    event: EventCreate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.UNIVERSITY]:
        return await event_response_handler.create(model_create=event, session=session)
    else:
        return access_denied()


@event_router.put("/{event_id}", response_model=Response)
async def update_event(
    user_id: int | None,
    event: EventUpdate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await event_response_handler.update(model_update=event, session=session)
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_event(
            user_id=user_id, event_id=event.id, session=session
        ):
            return await event_response_handler.update(
                model_update=event, session=session
            )

    return access_denied()


@event_router.delete("/{event_id}", response_model=Response)
async def delete_event(
    user_id: int | None,
    event_id: int,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await event_response_handler.delete(model_id=event_id, session=session)
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_event(
            user_id=user_id, event_id=event_id, session=session
        ):
            return await event_response_handler.delete(
                model_id=event_id, session=session
            )

    return access_denied()


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
    category: CategoryCreate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await category_response_handler.create(
            model_create=category, session=session
        )
    else:
        return access_denied()


@category_router.put("/{category_id}", response_model=Response)
async def update_category(
    category: CategoryUpdate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await category_response_handler.update(
            model_update=category, session=session
        )
    else:
        return access_denied()


@category_router.delete("/{category_id}", response_model=Response)
async def delete_category(
    category_id: int,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await category_response_handler.delete(
            model_id=category_id, session=session
        )
    else:
        return access_denied()


@tag_router.get("/", response_model=Response)
async def get_tags(
    event_id: Annotated[int | None, Query()] = None,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await tag_response_handler.get_by_filter(event_id=event_id, session=session)


@tag_router.get("/{tag_id}", response_model=Response)
async def get_tag_by_id(
    tag_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tag_response_handler.get_by_id(model_id=tag_id, session=session)


@tag_router.post("/", response_model=Response)
async def create_tag(
    tag: TagCreate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await tag_response_handler.create(model_create=tag, session=session)
    else:
        return access_denied()


@tag_router.put("/{tag_id}", response_model=Response)
async def update_tag(
    tag: TagUpdate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await tag_response_handler.update(model_update=tag, session=session)
    else:
        return access_denied()


@tag_router.delete("/{tag_id}", response_model=Response)
async def delete_tag(
    tag_id: int,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.ADMIN]:
        return await tag_response_handler.delete(model_id=tag_id, session=session)
    else:
        return access_denied()


@event_router.post("/{event_id}/tag", response_model=Response)
async def set_tags(
    event_tag: EventTagListCreate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await event_tag_response_handler.create_list(
            model_create=event_tag, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_event(
            user_id=user_id, event_id=event_tag.event_id, session=session
        ):
            return await event_tag_response_handler.create_list(
                model_create=event_tag, session=session
            )

    return access_denied()


@event_router.delete("/{event_id}/tag", response_model=Response)
async def delete_event_tag(
    event_tags: EventTagListDelete,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await event_tag_response_handler.delete_by_delete_schema(
            model_delete=event_tags, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_event(
            user_id=user_id, event_id=event_tags.event_id, session=session
        ):
            return await event_tag_response_handler.delete_by_delete_schema(
                model_delete=event_tags, session=session
            )

    return access_denied()


@event_router.get("/{event_id}/user", response_model=Response)
async def get_users_by_event(
    user_role: Role,
    user_id: int | None,
    event_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_event_response_handler.get_by_filter(
            user_event_filter=UserEventFilter.EVENT, value=event_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if check_university_event(user_id=user_id, event_id=event_id, session=session):
            return await user_event_response_handler.get_by_filter(
                user_event_filter=UserEventFilter.EVENT, value=event_id, session=session
            )

    return access_denied()
