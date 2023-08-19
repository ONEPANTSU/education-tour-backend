from src.database_utils.text.base_data_key import BaseDataKey

count = "university_events_count"
schemas = "university_events"
schema = "university_event"

UNIVERSITY_EVENT_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UniversityEventDataKey(BaseDataKey):
    _data_key: dict = UNIVERSITY_EVENT_DATA_KEY
