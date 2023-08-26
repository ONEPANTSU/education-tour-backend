from typing import Annotated

from fastapi import APIRouter, Depends, Query, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.schemas import Response
from src.university_module.database.university.university_responses import (
    UniversityResponseHandler,
)
from src.university_module.database.university_event.university_event_responses import (
    UniversityEventResponseHandler,
)
from src.university_module.database.university_tour.university_tour_responses import (
    UniversityTourResponseHandler,
)
from src.university_module.schemas import (
    UniversityCreate,
    UniversityEventListCreate,
    UniversityEventListDelete,
    UniversityTourListCreate,
    UniversityTourListDelete,
    UniversityUpdate,
)
from src.university_module.utils import check_user_university
from src.user_module.database.user_university.user_university_models import (
    UserUniversityFilter,
)
from src.user_module.router import user_university_response_handler
from src.utils import Role, access_denied, role_access

university_router = APIRouter(prefix="/university", tags=["university"])

university_response_handler = UniversityResponseHandler()
university_tour_response_handler = UniversityTourResponseHandler()
university_event_response_handler = UniversityEventResponseHandler()


@university_router.get("/", response_model=Response)
async def get_all_universities(
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await university_response_handler.get_all(session=session)


@university_router.get("/{university_id}", response_model=Response)
async def get_university_by_id(
    university_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_response_handler.get_by_id(
        model_id=university_id, session=session
    )


@university_router.post("/", response_model=Response)
async def create_university(
    user_role: Role,
    university: UniversityCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] >= role_access[Role.UNIVERSITY]:
        return await university_response_handler.create(
            model_create=university, session=session
        )

    return access_denied()


@university_router.put("/{university_id}", response_model=Response)
async def update_university(
    user_role: Role,
    user_id: int | None,
    university: UniversityUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_response_handler.update(
            model_update=university, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id, university_id=university.id, session=session
        ):
            return await university_response_handler.update(
                model_update=university, session=session
            )

    return access_denied()


@university_router.delete("/{university_id}", response_model=Response)
async def delete_university(
    user_role: Role,
    user_id: int | None,
    university_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_response_handler.delete(
            model_id=university_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id, university_id=university_id, session=session
        ):
            return await university_response_handler.delete(
                model_id=university_id, session=session
            )

    return access_denied()


@university_router.post("/image", response_model=Response)
async def update_image(
    image: UploadFile,
    university_id: int,
    user_id: Annotated[int | None, Query()] = None,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_response_handler.update_image(
            image=image, model_id=university_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id, university_id=university_id, session=session
        ):
            return await university_response_handler.update_image(
                image=image, model_id=university_id, session=session
            )
    else:
        return access_denied()


@university_router.delete("/image", response_model=Response)
async def delete_image(
    university_id: int,
    user_id: Annotated[int | None, Query()] = None,
    user_role: Annotated[Role, Query()] = Role.GUEST,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_response_handler.delete_image(
            model_id=university_id, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id, university_id=university_id, session=session
        ):
            return await university_response_handler.delete_image(
                model_id=university_id, session=session
            )
    else:
        return access_denied()


@university_router.post("/{university_id}/event", response_model=Response)
async def set_events(
    user_role: Role,
    user_id: int | None,
    university_event: UniversityEventListCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_event_response_handler.create_list(
            model_create=university_event, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id,
            university_id=university_event.university_id,
            session=session,
        ):
            return await university_event_response_handler.create_list(
                model_create=university_event, session=session
            )

    return access_denied()


@university_router.delete("/{university_id}/event", response_model=Response)
async def delete_university_event(
    user_role: Role,
    user_id: int | None,
    university_event: UniversityEventListDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_event_response_handler.delete_by_delete_schema(
            model_delete=university_event, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id,
            university_id=university_event.university_id,
            session=session,
        ):
            return await university_event_response_handler.delete_by_delete_schema(
                model_delete=university_event, session=session
            )

    return access_denied()


@university_router.post("/{university_id}/tour", response_model=Response)
async def set_tours(
    user_role: Role,
    user_id: int | None,
    university_tour: UniversityTourListCreate,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_tour_response_handler.create_list(
            model_create=university_tour, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id,
            university_id=university_tour.university_id,
            session=session,
        ):
            return await university_tour_response_handler.create_list(
                model_create=university_tour, session=session
            )

    return access_denied()


@university_router.delete("/{university_id}/tour", response_model=Response)
async def delete_university_tour(
    user_role: Role,
    user_id: int | None,
    university_tour: UniversityTourListDelete,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    if role_access[user_role] == role_access[Role.ADMIN]:
        return await university_tour_response_handler.delete_by_delete_schema(
            model_delete=university_tour, session=session
        )
    elif role_access[user_role] == role_access[Role.UNIVERSITY] and user_id is not None:
        if await check_user_university(
            user_id=user_id,
            university_id=university_tour.university_id,
            session=session,
        ):
            return await university_tour_response_handler.delete_by_delete_schema(
                model_delete=university_tour, session=session
            )

    return access_denied()


@university_router.post("/{university_id}/user", response_model=Response)
async def get_user_by_university_id(
    university_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_university_response_handler.get_by_filter(
        user_university_filter=UserUniversityFilter.UNIVERSITY,
        value=university_id,
        session=session,
    )
