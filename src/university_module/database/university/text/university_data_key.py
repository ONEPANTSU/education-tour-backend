from src.database_utils.text.base_data_key import BaseDataKey

count = "universities_count"
schemas = "universities"
schema = "university"

UNIVERSITY_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UniversityDataKey(BaseDataKey):
    _data_key: dict = UNIVERSITY_DATA_KEY
