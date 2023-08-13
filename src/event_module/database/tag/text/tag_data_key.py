from src.database_utils.text.base_data_key import BaseDataKey

count = "tags_count"
schemas = "tags"
schema = "tag"

TAG_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class TagDataKey(BaseDataKey):
    _data_key: dict = TAG_DATA_KEY
