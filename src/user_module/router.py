from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.schemas import Response
from src.user_module.database.user_event.user_event_models import UserEventFilter
from src.user_module.database.user_event.user_event_responses import (
    UserEventResponseHandler,
)
from src.user_module.database.user_tour.user_tour_models import UserTourFilter
from src.user_module.database.user_tour.user_tour_responses import (
    UserTourResponseHandler,
)
from src.user_module.schemas import (
    UserEventCreate,
    UserEventDelete,
    UserTourCreate,
    UserTourDelete,
)

user_router = APIRouter(prefix="/user", tags=["user"])

user_tour_response_handler = UserTourResponseHandler()
user_event_response_handler = UserEventResponseHandler()


@user_router.post("/{user_id}/set_event", response_model=Response)
async def set_event(
    user_event: UserEventCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_event_response_handler.create(
        model_create=user_event, session=session
    )


@user_router.get("/{user_id}/events", response_model=Response)
async def get_events(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_event_response_handler.get_by_filter(
        user_event_filter=UserEventFilter.USER, value=user_id, session=session
    )


@user_router.get("/{event_id}", response_model=Response)
async def get_users_by_event(
    event_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_event_response_handler.get_by_filter(
        user_event_filter=UserEventFilter.EVENT, value=event_id, session=session
    )


@user_router.delete("/{user_id}/{event_id}", response_model=Response)
async def delete_user_event(
    user_event: UserEventDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_event_response_handler.delete_by_delete_schema(
        model_delete=user_event, session=session
    )


@user_router.delete("/{user_id}/events", response_model=Response)
async def delete_all_user_events(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_event_response_handler.delete_by_user(
        user_id=user_id, session=session
    )


@user_router.post("/{user_id}/set_tour", response_model=Response)
async def set_tour(
    user_tour: UserTourCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_tour_response_handler.create(user_tour=user_tour, session=session)


@user_router.get("/{user_id}/tours", response_model=Response)
async def get_tours(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_tour_response_handler.get_by_filter(
        user_tour_filter=UserTourFilter.USER, value=user_id, session=session
    )


@user_router.get("/{tour_id}", response_model=Response)
async def get_users_by_tour(
    tour_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_tour_response_handler.get_by_filter(
        user_tour_filter=UserTourFilter.TOUR, value=tour_id, session=session
    )


@user_router.delete("/{user_id}/{tour_id}", response_model=Response)
async def delete_user_tour(
    user_tour: UserTourDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_tour_response_handler.delete_by_delete_schema(
        model_delete=user_tour, session=session
    )


@user_router.delete("/{user_id}/tours", response_model=Response)
async def delete_all_user_events(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_tour_response_handler.delete_by_user(
        user_id=user_id, session=session
    )
