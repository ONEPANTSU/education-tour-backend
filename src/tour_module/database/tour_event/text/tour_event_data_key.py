from src.database_utils.text.base_data_key import BaseDataKey

count = "tour_events_count"
schemas = "tour_events"
schema = "tour_event"

TOUR_EVENT_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class TourEventDataKey(BaseDataKey):
    _data_key: dict = TOUR_EVENT_DATA_KEY
