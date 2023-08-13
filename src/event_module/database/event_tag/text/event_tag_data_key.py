from src.database_utils.text.base_data_key import BaseDataKey

count = "event_tags_count"
schemas = "event_tags"
schema = "event_tag"

EVENT_TAG_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class EventTagDataKey(BaseDataKey):
    _data_key: dict = EVENT_TAG_DATA_KEY
