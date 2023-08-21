from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.university_module.database.university_event.text.university_event_data_key import (
    UniversityEventDataKey,
)
from src.university_module.database.university_event.university_event_responses import (
    UniversityEventResponseHandler,
)


async def check_university_event(
    university_id: int, event_id: int, session: AsyncSession
):
    events = (
        (
            await UniversityEventResponseHandler().get_by_filter(
                value=university_id, session=session
            )
        )
        .data[UniversityEventDataKey().get(key="schemas")]
        .event_id_list
    )
    return event_id in events
