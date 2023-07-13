from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.event_module.schemas import EventCreate, EventUpdate
from src.event_module.utils.event.queries import (
    create_event_query,
    delete_event_query,
    get_all_events_query,
    get_event_by_id_query,
    get_events_by_category_query,
    update_event_query,
)
from src.event_module.utils.event.text.details import DETAILS
from src.event_module.utils.event.text.messages import MESSAGE
from src.utils import STATUS, return_json


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
async def get_events_by_category_response(
    category_id: int, session: AsyncSession
) -> dict:
    try:
        events = await get_events_by_category_query(
            category_id=category_id, session=session
        )
        if events is not None:
            data = {"events_count": len(events), "events": events}
            return return_json(
                status=STATUS[200],
                message=MESSAGE["get_events_by_category_success"].format(
                    category_id=category_id
                ),
                data=data,
            )
        else:
            raise Exception()
    except Exception as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_events_by_category_error"],
            details=str(e),
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
async def update_event_response(event: EventUpdate, session: AsyncSession) -> dict:
    try:
        if event.id in [
            existing.id for existing in await get_all_events_query(session=session)
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
async def delete_event_response(event_id: int, session: AsyncSession) -> dict:
    try:
        if event_id in [
            existing.id for existing in await get_all_events_query(session=session)
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
