from sqlalchemy.ext.asyncio import AsyncSession

from src.university_module.database.university_tour.text.university_tour_data_key import (
    UniversityTourDataKey,
)
from src.university_module.database.university_tour.university_tour_responses import (
    UniversityTourResponseHandler,
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


async def check_university_tour(user_id: int, tour_id: int, session: AsyncSession):
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
    tours = (
        (
            await UniversityTourResponseHandler().get_by_filter(
                value=university_id, session=session
            )
        )
        .data[UniversityTourDataKey().get(key="schemas")]
        .event_id_list
    )
    return tour_id in tours
