from fastapi import APIRouter, Depends
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
from src.user_module.database.user_university.user_university_models import UserUniversityFilter
from src.user_module.router import user_university_response_handler

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
        university: UniversityCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_response_handler.create(
        model_create=university, session=session
    )


@university_router.put("/{university_id}", response_model=Response)
async def update_university(
        university: UniversityUpdate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_response_handler.update(
        model_update=university, session=session
    )


@university_router.delete("/{university_id}", response_model=Response)
async def delete_university(
        university_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await university_response_handler.delete(
        model_id=university_id, session=session
    )


@university_router.post("/{university_id}/set_events", response_model=Response)
async def set_events(
        university_event: UniversityEventListCreate,
        session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await university_event_response_handler.create_list(
        model_create=university_event, session=session
    )


@university_router.delete("/{university_id}/university_event", response_model=Response)
async def delete_university_event(
        university_event: UniversityEventListDelete,
        session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await university_event_response_handler.delete_by_delete_schema(
        model_delete=university_event, session=session
    )


@university_router.post("/{university_id}/set_tours", response_model=Response)
async def set_tours(
        university_tour: UniversityTourListCreate,
        session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await university_tour_response_handler.create_list(
        model_create=university_tour, session=session
    )


@university_router.delete("/{university_id}/university_tour", response_model=Response)
async def delete_university_tour(
        university_tour: UniversityTourListDelete,
        session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await university_tour_response_handler.delete_by_delete_schema(
        model_delete=university_tour, session=session
    )


@university_router.post("/{university_id}/user", response_model=Response)
async def get_user_by_university_id(
        university_id: int,
        session: AsyncSession = Depends(get_async_session),
) -> Response:
    return await user_university_response_handler.get_by_filter(
        user_university_filter=UserUniversityFilter.UNIVERSITY, value=university_id, session=session
    )
