from typing import List, Optional

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.event.models import Event
from src.event.schemas import EventCreate, EventRead, EventUpdate
from src.event.text.details import DETAILS
from src.event.text.messages import MESSAGE
from src.utils import STATUS, return_json


@logger.catch
def convert_row_to_event(event_row: Event) -> Optional[List[Event]]:
    event = Event(
        id=event_row[0].id,
        name=event_row[0].name,
        description=event_row[0].description,
        date_start=event_row[0].date_start,
        date_end=event_row[0].date_end,
        reg_deadline=event_row[0].reg_deadline,
        max_users=event_row[0].max_users,
        category_id=event_row[0].category_id,
        address=event_row[0].address,
    )
    return event


@logger.catch
def convert_rows_to_event_list(event_rows: List[Event]) -> Optional[List[Event]]:
    return [convert_row_to_event(event_row=event_row) for event_row in event_rows]


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
async def get_all_events_response(session: AsyncSession) -> dict:
    try:
        events = await get_all_events_query(session=session)
        if events is not None:
            data = {"events_count": len(events), "events": events}
            return return_json(
                status=STATUS[200], message=MESSAGE["get_all_events_success"], data=data
            )
        else:
            raise Exception()
    except Exception as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400], message=MESSAGE["get_all_events_error"], details=str(e)
        )


@logger.catch
async def get_event_by_id_response(event_id: int, session: AsyncSession) -> dict:
    try:
        event = await get_event_by_id_query(event_id=event_id, session=session)
        if event is not None:
            data = {"event": event}
            return return_json(
                status=STATUS[200],
                message=MESSAGE["get_one_event_success"].format(event_id=event_id),
                data=data,
            )
        else:
            raise Exception()
    except Exception as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_one_event_error"].format(event_id=event_id),
            details=str(e),
        )


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
async def create_event_response(event: EventCreate, session: AsyncSession) -> dict:
    try:
        error = await create_event_query(event=event, session=session)
        if error is None:
            return return_json(
                status=STATUS[200], message=MESSAGE["create_event_success"]
            )
        else:
            raise error
    except IntegrityError as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["create_event_error"],
            details=DETAILS["wrong_category_id"],
        )


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
async def update_event_response(event: EventUpdate, session: AsyncSession) -> dict:
    try:
        if event.id in [
            existing.id
            for existing in await get_all_events_query(session=session)
        ]:
            error = await update_event_query(event=event, session=session)
            if error is None:
                return return_json(
                    status=STATUS[200],
                    message=MESSAGE["update_event_success"].format(event_id=event.id),
                )
            else:
                raise error
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["update_event_error"].format(event_id=event.id),
                details=DETAILS["wrong_event_id"].format(event_id=event.id),
            )
    except IntegrityError as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["update_event_error"].format(event_id=event.id),
        )


@logger.catch
async def delete_event_query(
    event_id: int, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        await session.execute(delete(Event).where(Event.id == event_id))
        await session.commit()
    except IntegrityError as e:
        return e


@logger.catch
async def delete_event_response(event_id: int, session: AsyncSession) -> dict:
    try:
        if event_id in [
            existing.id
            for existing in await get_all_events_query(session=session)
        ]:
            error = await delete_event_query(event_id=event_id, session=session)
            if error is None:
                return return_json(
                    status=STATUS[200],
                    message=MESSAGE["delete_event_success"].format(event_id=event_id),
                )
            else:
                raise error
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["delete_event_error"].format(event_id=event_id),
                details=DETAILS["wrong_event_id"].format(event_id=event_id),
            )
    except IntegrityError as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["delete_event_error"].format(event_id=event_id),
        )
