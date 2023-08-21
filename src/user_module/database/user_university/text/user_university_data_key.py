from src.database_utils.text.base_data_key import BaseDataKey

count = "user_universities_count"
schemas = "user_universities"
schema = "user_university"

USER_UNIVERSITY_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class UserUniversityDataKey(BaseDataKey):
    _data_key: dict = USER_UNIVERSITY_DATA_KEY
