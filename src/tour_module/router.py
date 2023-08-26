from typing import Annotated

from fastapi import APIRouter, Depends, Query, UploadFile
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
from src.user_module.database.user_tour.user_tour_models import UserTourFilter
from src.user_module.router import user_tour_response_handler
from src.utils import Role, access_denied, role_access

tour_router = APIRouter(prefix="/tour", tags=["tour"])

tour_response_handler = TourResponseHandler()
tour_event_response_handler = TourEventResponseHandler()


@tour_router.get("/", response_model=Response)
async def get_all_tours(
    university_id: Annotated[int | None, Query()] = None,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await tour_response_handler.get_by_filter(
        university_id=university_id, session=session
    )


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
    tour: TourUpdate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
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
    tour_id: int,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
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


@tour_router.post("/image", response_model=Response)
async def update_image(
    image: UploadFile,
    tour_id: int,
    user_id: Annotated[int | None, Query()] = None,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_response_handler.update_image(
            image=image, model_id=tour_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour_id, session=session
        ):
            return await tour_response_handler.update_image(
                image=image, model_id=tour_id, session=session
            )
    else:
        return access_denied()


@tour_router.delete("/image", response_model=Response)
async def delete_image(
    tour_id: int,
    user_id: Annotated[int | None, Query()] = None,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await tour_response_handler.delete_image(
            model_id=tour_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_university_tour(
            user_id=user_id, tour_id=tour_id, session=session
        ):
            return await tour_response_handler.delete_image(
                model_id=tour_id, session=session
            )
    else:
        return access_denied()


@tour_router.post("/{tour_id}/event", response_model=Response)
async def set_events(
    tour_event: TourEventListCreate,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
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


@tour_router.delete("/{tour_id}/event", response_model=Response)
async def delete_tour_event(
    tour_event: TourEventListDelete,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    user_id: Annotated[int | None, Query()] = None,
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


@tour_router.get("/{tour_id}/user", response_model=Response)
async def get_users_by_tour(
    user_role: Role,
    tour_id: int,
    user_id: Annotated[int | None, Query()] = None,
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
