from typing import List, Optional

from loguru import logger

from src.event_module.models import Event


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
