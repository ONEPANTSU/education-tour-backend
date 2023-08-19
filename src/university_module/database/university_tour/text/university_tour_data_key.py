from src.database_utils.text.base_data_key import BaseDataKey

count = "university_tours_count"
schemas = "university_tours"
schema = "university_tour"

UNIVERSITY_TOUR_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UniversityTourDataKey(BaseDataKey):
    _data_key: dict = UNIVERSITY_TOUR_DATA_KEY
