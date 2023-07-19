from typing import List, Optional

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.event_module.models import Event
from src.event_module.schemas import EventCreate, EventRead, EventUpdate
from src.event_module.utils.event.utils import (
    convert_row_to_event,
    convert_rows_to_event_list,
)


@logger.catch
async def get_all_events_query(session: AsyncSession) -> Optional[List[EventRead]]:
    try:
        event_rows = await session.execute(select(Event))
        events = convert_rows_to_event_list(event_rows=event_rows.all())
        return events
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def get_events_by_categories_query(
    category_list: List[int], session: AsyncSession
) -> Optional[List[EventRead]]:
    try:
        events = []
        for category_id in category_list:
            event_rows = await session.execute(
                select(Event).filter(Event.category_id == category_id)
            )
            events += convert_rows_to_event_list(event_rows=event_rows.all())
        return events
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def get_events_by_category_query(
    category_id: int, session: AsyncSession
) -> Optional[List[EventRead]]:
    try:
        event_rows = await session.execute(
            select(Event).filter(Event.category_id == category_id)
        )
        events = convert_rows_to_event_list(event_rows=event_rows.all())
        return events
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def get_event_by_id_query(
    event_id: int, session: AsyncSession
) -> Optional[EventRead]:
    try:
        event_rows = await session.execute(select(Event).filter(Event.id == event_id))
        event = convert_row_to_event(event_row=event_rows.one())
        return event
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def create_event_query(
    event: EventCreate, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        event.fix_time()
        await session.execute(insert(Event).values(**event.dict()))
        await session.commit()
    except IntegrityError as e:
        return e


@logger.catch
async def update_event_query(
    event: EventUpdate, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        event.fix_time()
        await session.execute(
            update(Event).values(**event.dict()).where(Event.id == event.id)
        )
        await session.commit()
    except IntegrityError as e:
        return e


@logger.catch
async def delete_event_query(
    event_id: int, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        await session.execute(delete(Event).where(Event.id == event_id))
        await session.commit()
    except IntegrityError as e:
        return e
