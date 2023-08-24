from sqlalchemy.ext.asyncio import AsyncSession

from src.university_module.database.university_event.text.university_event_data_key import (
    UniversityEventDataKey,
)
from src.university_module.database.university_event.university_event_responses import (
    UniversityEventResponseHandler,
)
from src.user_module.database.user_university.text.user_university_data_key import (
    UserUniversityDataKey,
)
from src.user_module.database.user_university.user_university_models import (
    UserUniversityFilter,
)
from src.user_module.database.user_university.user_university_responses import (
    UserUniversityResponseHandler,
)


async def check_university_event(user_id: int, event_id: int, session: AsyncSession):
    university_id = (
        (
            await UserUniversityResponseHandler().get_by_filter(
                user_university_filter=UserUniversityFilter.USER,
                value=user_id,
                session=session,
            )
        )
        .data[UserUniversityDataKey().get(key="schema")]
        .university_id
    )
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
