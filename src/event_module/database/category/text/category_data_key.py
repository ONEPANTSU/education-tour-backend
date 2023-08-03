from src.database_utils.text.base_data_key import BaseDataKey

count = "categories_count"
schemas = "categories"
schema = "category"

CATEGORY_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class CategoryDataKey(BaseDataKey):
    _data_key: dict = CATEGORY_DATA_KEY
