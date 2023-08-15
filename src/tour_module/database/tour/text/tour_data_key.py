from src.database_utils.text.base_data_key import BaseDataKey

count = "tours_count"
schemas = "tours"
schema = "tour"

TOUR_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class TourDataKey(BaseDataKey):
    _data_key: dict = TOUR_DATA_KEY
