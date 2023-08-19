from src.database_utils.text.base_data_key import BaseDataKey

count = "user_events_count"
schemas = "user_events"
schema = "user_event"

USER_EVENT_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UserEventDataKey(BaseDataKey):
    _data_key: dict = USER_EVENT_DATA_KEY
