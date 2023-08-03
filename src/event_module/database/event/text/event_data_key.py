from src.database_utils.text.base_data_key import BaseDataKey

count = "events_count"
schemas = "events"
schema = "event"

EVENT_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class EventDataKey(BaseDataKey):
    _data_key: dict = EVENT_DATA_KEY
