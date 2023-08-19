from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы university_event"

UNIVERSITY_EVENT_DETAILS = {
    "wrong_id": wrong_id,
}


class UniversityEventDetails(BaseDetails):
    _details = UNIVERSITY_EVENT_DETAILS
