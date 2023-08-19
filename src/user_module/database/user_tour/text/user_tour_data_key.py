from src.database_utils.text.base_data_key import BaseDataKey

count = "user_tours_count"
schemas = "user_tours"
schema = "user_tour"

USER_TOUR_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UserTourDataKey(BaseDataKey):
    _data_key: dict = USER_TOUR_DATA_KEY
