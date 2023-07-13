from typing import List, Optional

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.event_module.models import Category
from src.event_module.schemas import CategoryCreate, CategoryRead, CategoryUpdate
from src.event_module.utils.category.utils import (
    convert_row_to_category,
    convert_rows_to_category_list,
)


@logger.catch
async def get_all_categories_query(
    session: AsyncSession,
) -> Optional[List[CategoryRead]]:
    try:
        category_rows = await session.execute(select(Category))
        categories = convert_rows_to_category_list(category_rows=category_rows.all())
        return categories
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def get_category_by_id_query(
    category_id: int, session: AsyncSession
) -> Optional[CategoryRead]:
    try:
        category_rows = await session.execute(
            select(Category).filter(Category.id == category_id)
        )
        category = convert_row_to_category(category_row=category_rows.one())
        return category
    except Exception as e:
        logger.error(str(e))
        return None


@logger.catch
async def create_category_query(
    category: CategoryCreate, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        await session.execute(insert(Category).values(**category.dict()))
        await session.commit()
    except Exception as e:
        return e


@logger.catch
async def update_category_query(
    category: CategoryUpdate, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        await session.execute(
            update(Category).values(**category.dict()).where(Category.id == category.id)
        )
        await session.commit()
    except Exception as e:
        return e


@logger.catch
async def delete_category_query(
    category_id: int, session: AsyncSession
) -> Optional[IntegrityError]:
    try:
        await session.execute(delete(Category).where(Category.id == category_id))
        await session.commit()
    except IntegrityError as e:
        return e
