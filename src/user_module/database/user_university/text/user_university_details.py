from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы user_university"

USER_UNIVERSITY_DETAILS = {
    "wrong_id": wrong_id,
}


class UserUniversityDetails(BaseDetails):
    _details = USER_UNIVERSITY_DETAILS
