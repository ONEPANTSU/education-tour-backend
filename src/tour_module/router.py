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
    tour: TourCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_response_handler.create(model_create=tour, session=session)


@tour_router.put("/{tour_id}", response_model=Response)
async def update_tour(
    tour: TourUpdate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_response_handler.update(model_update=tour, session=session)


@tour_router.delete("/{tour_id}", response_model=Response)
async def delete_tour(
    tour_id: int, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_response_handler.delete(model_id=tour_id, session=session)


@tour_router.post("/{tour_id}/set_events", response_model=Response)
async def set_events(
    tour_event: TourEventListCreate, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_event_response_handler.create_list(
        model_create=tour_event, session=session
    )


@tour_router.delete("/{tour_id}/tour_event", response_model=Response)
async def delete_tour_event(
    tour_event: TourEventListDelete, session: AsyncSession = Depends(get_async_session)
) -> Response:
    return await tour_event_response_handler.delete_by_delete_schema(
        model_delete=tour_event, session=session
    )
