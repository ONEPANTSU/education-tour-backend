from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.event_module.schemas import CategoryCreate, CategoryUpdate
from src.event_module.utils.category.queries import (
    create_category_query,
    delete_category_query,
    get_all_categories_query,
    get_category_by_id_query,
    update_category_query,
)
from src.event_module.utils.category.text.details import DETAILS
from src.event_module.utils.category.text.messages import MESSAGE
from src.event_module.utils.event.queries import get_all_events_query
from src.utils import STATUS, return_json


@logger.catch
async def get_all_categories_response(session: AsyncSession) -> dict:
    try:
        categories = await get_all_categories_query(session=session)
        if categories is not None:
            data = {"categories_count": len(categories), "categories": categories}
            return return_json(
                status=STATUS[200],
                message=MESSAGE["get_all_categories_success"],
                data=data,
            )
        else:
            raise Exception()
    except Exception as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_all_categories_error"],
            details=str(e),
        )


@logger.catch
async def get_category_by_id_response(category_id: int, session: AsyncSession) -> dict:
    try:
        category = await get_category_by_id_query(
            category_id=category_id, session=session
        )
        if category is not None:
            data = {"category": category}
            return return_json(
                status=STATUS[200],
                message=MESSAGE["get_one_category_success"].format(
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
            message=MESSAGE["get_one_category_error"].format(category_id=category_id),
            details=str(e),
        )


@logger.catch
async def create_category_response(
    category: CategoryCreate, session: AsyncSession
) -> dict:
    try:
        error = await create_category_query(category=category, session=session)
        if error is None:
            return return_json(
                status=STATUS[200], message=MESSAGE["create_category_success"]
            )
        else:
            raise error
    except Exception as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["create_category_error"],
            details=str(e),
        )


@logger.catch
async def update_category_response(
    category: CategoryUpdate, session: AsyncSession
) -> dict:
    try:
        if category.id in [
            existing.id for existing in await get_all_categories_query(session=session)
        ]:
            error = await update_category_query(category=category, session=session)
            if error is None:
                return return_json(
                    status=STATUS[200],
                    message=MESSAGE["update_category_success"].format(
                        category_id=category.id
                    ),
                )
            else:
                raise error
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["update_category_error"].format(
                    category_id=category.id
                ),
                details=DETAILS["wrong_category_id"].format(category_id=category.id),
            )
    except IntegrityError as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["update_category_error"].format(category_id=category.id),
        )


@logger.catch
async def delete_category_response(category_id: int, session: AsyncSession) -> dict:
    try:
        if category_id not in [
            existing_event.category_id
            for existing_event in await get_all_events_query(session=session)
        ]:
            if category_id in [
                existing.id
                for existing in await get_all_categories_query(session=session)
            ]:
                error = await delete_category_query(
                    category_id=category_id, session=session
                )
                if error is None:
                    return return_json(
                        status=STATUS[200],
                        message=MESSAGE["delete_category_success"].format(
                            category_id=category_id
                        ),
                    )
                else:
                    raise error
            else:
                return return_json(
                    status=STATUS[400],
                    message=MESSAGE["delete_category_error"].format(
                        category_id=category_id
                    ),
                    details=DETAILS["wrong_category_id"].format(
                        category_id=category_id
                    ),
                )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["delete_category_error"].format(
                    category_id=category_id
                ),
                details=DETAILS["trying_to_delete_category_foreign_key"].format(
                    category_id=category_id
                ),
            )
    except IntegrityError as e:
        logger.error(str(e))
        return return_json(
            status=STATUS[400],
            message=MESSAGE["delete_category_error"].format(category_id=category_id),
        )
