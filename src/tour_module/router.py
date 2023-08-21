from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.schemas import Response
from src.tour_module.database.tour.tour_responses import TourResponseHandler
from src.tour_module.database.tour_event.tour_event_responses import (
    TourEventResponseHandler,
)
from src.tour_module.schemas import (
    TourCreate,
    TourEventListCreate,
    TourEventListDelete,
    TourUpdate,
)
from src.tour_module.utils import check_university_tour
from src.university_module.router import university_tour_response_handler
from src.utils import Role, access_denied, role_access

tour_router = APIRouter(prefix="/tour", tags=["tour"])

tour_response_handler = TourResponseHandler()
tour_event_response_handler = TourEventResponseHandler()


@tour_router.get("/", response_model=Response)
async def get_all_tours(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await tour_response_handler.get_all(session=session)


@tour_router.get("/{tour_id}", response_model=Response)
async def get_tour_by_id(
    tour_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_response_handler.get_by_id(model_id=tour_id, session=session)


@tour_router.post("/", response_model=Response)
async def create_tour(
    user_role: Role,
    tour: TourCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.UNIVERSITY]:
        return await tour_response_handler.create(model_create=tour, session=session)

    return access_denied()


@tour_router.put("/{tour_id}", response_model=Response)
async def update_tour(
    user_role: Role,
    user_id: int | None,
    tour: TourUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_response_handler.update(model_update=tour, session=session)
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour.id, session=session
        ):
            return await tour_response_handler.update(
                model_update=tour, session=session
            )

    return access_denied()


@tour_router.delete("/{tour_id}", response_model=Response)
async def delete_tour(
    user_role: Role,
    user_id: int | None,
    tour_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_response_handler.delete(model_id=tour_id, session=session)
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour_id, session=session
        ):
            return await tour_response_handler.delete(model_id=tour_id, session=session)

    return access_denied()


@tour_router.post("/{tour_id}/set_events", response_model=Response)
async def set_events(
    user_role: Role,
    user_id: int | None,
    tour_event: TourEventListCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_event_response_handler.create_list(
            model_create=tour_event, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour_event.tour_id, session=session
        ):
            return await tour_event_response_handler.create_list(
                model_create=tour_event, session=session
            )

    return access_denied()


@tour_router.delete("/{tour_id}/tour_event", response_model=Response)
async def delete_tour_event(
    user_role: Role,
    user_id: int | None,
    tour_event: TourEventListDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_event_response_handler.delete_by_delete_schema(
            model_delete=tour_event, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour_event.tour_id, session=session
        ):
            return await tour_event_response_handler.delete_by_delete_schema(
                model_delete=tour_event, session=session
            )

    return access_denied()


@tour_router.get("/university_filter/{university_id}", response_model=Response)
async def get_tour_id_list_by_university_id(
    university_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_tour_response_handler.get_by_filter(
        value=university_id, session=session
    )
