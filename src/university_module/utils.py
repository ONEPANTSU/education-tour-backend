from sqlalchemy.ext.asyncio import AsyncSession

from src.user_module.database.user_university.text.user_university_data_key import (
    UserUniversityDataKey,
)
from src.user_module.database.user_university.user_university_models import (
    UserUniversityFilter,
)
from src.user_module.database.user_university.user_university_responses import (
    UserUniversityResponseHandler,
)


async def check_user_university(
    user_id: int, university_id: int, session: AsyncSession
):
    existing_university_id = (
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
    return (
        existing_university_id is not None and university_id == existing_university_id
    )
