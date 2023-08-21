from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.event_module.utils import check_university_event
from src.schemas import Response
from src.tour_module.utils import check_university_tour
from src.user_module.database.user_event.user_event_models import UserEventFilter
from src.user_module.database.user_event.user_event_responses import (
    UserEventResponseHandler,
)
from src.user_module.database.user_tour.user_tour_models import UserTourFilter
from src.user_module.database.user_tour.user_tour_responses import (
    UserTourResponseHandler,
)
from src.user_module.database.user_university.user_university_models import (
    UserUniversityFilter,
)
from src.user_module.database.user_university.user_university_responses import (
    UserUniversityResponseHandler,
)
from src.user_module.schemas import (
    UserEventCreate,
    UserEventDelete,
    UserTourCreate,
    UserTourDelete,
    UserUniversityCreate,
)
from src.user_module.utils import check_user_ids
from src.utils import Role, access_denied, role_access

user_router = APIRouter(prefix="/user", tags=["user"])

user_tour_response_handler = UserTourResponseHandler()
user_event_response_handler = UserEventResponseHandler()
user_university_response_handler = UserUniversityResponseHandler()


@user_router.post("/{user_id}/set_event", response_model=Response)
async def set_event(
    user_role: Role,
    user_id: int | None,
    user_event: UserEventCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_event_response_handler.create(
            model_create=user_event, session=session
        )
    elif role_access[user_role] == role_access[Role.USER] and user_id is not None:
        if check_user_ids(needed=user_id, received=user_event.user_id):
            return await user_event_response_handler.create(
                model_create=user_event, session=session
            )

    return access_denied()


@user_router.get("/{user_id}/events", response_model=Response)
async def get_events(
    user_role: Role,
    user_id: int | None,
    user_id_to_get: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_event_response_handler.get_by_filter(
            user_event_filter=UserEventFilter.USER,
            value=user_id_to_get,
            session=session,
        )

    elif role_access[user_role] == role_access[Role.USER]:
        if check_user_ids(needed=user_id, received=user_id_to_get):
            return await user_event_response_handler.get_by_filter(
                user_event_filter=UserEventFilter.USER,
                value=user_id_to_get,
                session=session,
            )

    return access_denied()


@user_router.get("/{event_id}", response_model=Response)
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


@user_router.delete("/{user_id}/{event_id}", response_model=Response)
async def delete_user_event(
    user_role: Role,
    user_id: int | None,
    user_event: UserEventDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_event_response_handler.delete_by_delete_schema(
            model_delete=user_event, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if check_university_event(
            user_id=user_id, event_id=user_event.event_id, session=session
        ):
            return await user_event_response_handler.delete_by_delete_schema(
                model_delete=user_event, session=session
            )
    elif role_access[user_role] == role_access[Role.USER] and user_id is not None:
        if check_user_ids(needed=user_id, received=user_event.user_id):
            return await user_event_response_handler.delete_by_delete_schema(
                model_delete=user_event, session=session
            )

    return access_denied()


@user_router.delete("/{user_id}/events", response_model=Response)
async def delete_all_user_events(
    user_role: Role,
    user_id: int | None,
    user_id_to_delete: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_event_response_handler.delete_by_user(
            user_id=user_id_to_delete, session=session
        )

    elif role_access[user_role] == role_access[Role.USER]:
        if check_user_ids(needed=user_id, received=user_id_to_delete):
            return await user_event_response_handler.delete_by_user(
                user_id=user_id_to_delete, session=session
            )

    return access_denied()


@user_router.post("/{user_id}/set_tour", response_model=Response)
async def set_tour(
    user_role: Role,
    user_id: int | None,
    user_tour: UserTourCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_tour_response_handler.create(
            user_tour=user_tour, session=session
        )

    elif role_access[user_role] == role_access[Role.USER]:
        if check_user_ids(needed=user_id, received=user_tour.user_id):
            return await user_tour_response_handler.create(
                user_tour=user_tour, session=session
            )

    return access_denied()


@user_router.get("/{user_id}/tours", response_model=Response)
async def get_tours(
    user_role: Role,
    user_id: int | None,
    user_id_to_get: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_tour_response_handler.get_by_filter(
            user_tour_filter=UserTourFilter.USER, value=user_id_to_get, session=session
        )
    elif role_access[user_role] == role_access[Role.USER]:
        if check_user_ids(needed=user_id, received=user_id_to_get):
            return await user_tour_response_handler.get_by_filter(
                user_tour_filter=UserTourFilter.USER,
                value=user_id_to_get,
                session=session,
            )

    return access_denied()


@user_router.get("/{tour_id}", response_model=Response)
async def get_users_by_tour(
    user_role: Role,
    user_id: int | None,
    tour_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_tour_response_handler.get_by_filter(
            user_tour_filter=UserTourFilter.TOUR, value=tour_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if check_university_tour(user_id=user_id, tour_id=tour_id, session=session):
            return await user_tour_response_handler.get_by_filter(
                user_tour_filter=UserTourFilter.TOUR, value=tour_id, session=session
            )

    return access_denied()


@user_router.delete("/{user_id}/{tour_id}", response_model=Response)
async def delete_user_tour(
    user_role: Role,
    user_id: int | None,
    user_tour: UserTourDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_tour_response_handler.delete_by_delete_schema(
            model_delete=user_tour, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if check_university_tour(
            user_id=user_id, tour_id=user_tour.tour_id, session=session
        ):
            return await user_tour_response_handler.delete_by_delete_schema(
                model_delete=user_tour, session=session
            )
    elif role_access[user_role] == role_access[Role.USER] and user_id is not None:
        if check_user_ids(needed=user_id, received=user_tour.user_id):
            return await user_tour_response_handler.delete_by_delete_schema(
                model_delete=user_tour, session=session
            )

    return access_denied()


@user_router.delete("/{user_id}/tours", response_model=Response)
async def delete_all_user_events(
    user_role: Role,
    user_id: int | None,
    user_id_to_delete: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_tour_response_handler.delete_by_user(
            user_id=user_id_to_delete, session=session
        )

    elif role_access[user_role] == role_access[Role.USER]:
        if check_user_ids(needed=user_id, received=user_id_to_delete):
            return await user_tour_response_handler.delete_by_user(
                user_id=user_id_to_delete, session=session
            )

    return access_denied()


@user_router.post("/{user_id}/{university}", response_model=Response)
async def set_university(
    user_role: Role,
    user_university: UserUniversityCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.UNIVERSITY]:
        return await user_university_response_handler.create(
            model_create=user_university, session=session
        )

    return access_denied()


@user_router.get("/{user_id}/university", response_model=Response)
async def get_university_by_user_id(
    user_role: Role,
    user_id: int | None,
    user_id_to_get: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await user_university_response_handler.get_by_filter(
            user_university_filter=UserUniversityFilter.USER,
            value=user_id_to_get,
            session=session,
        )

    elif role_access[user_role] == role_access[Role.UNIVERSITY]:
        if check_user_ids(needed=user_id, received=user_id_to_get):
            return await user_university_response_handler.get_by_filter(
                user_university_filter=UserUniversityFilter.USER,
                value=user_id_to_get,
                session=session,
            )

    return access_denied()
