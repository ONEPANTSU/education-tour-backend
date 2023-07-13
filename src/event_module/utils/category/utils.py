from typing import List, Optional

from loguru import logger

from src.event_module.models import Category


@logger.catch
def convert_row_to_category(category_row: Category) -> Optional[List[Category]]:
    category = Category(
        id=category_row[0].id,
        name=category_row[0].name,
    )
    return category


@logger.catch
def convert_rows_to_category_list(
    category_rows: List[Category],
) -> Optional[List[Category]]:
    return [
        convert_row_to_category(category_row=category_row)
        for category_row in category_rows
    ]
