from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы user_event"

USER_EVENT_DETAILS = {
    "wrong_id": wrong_id,
}


class UserEventDetails(BaseDetails):
    _details = USER_EVENT_DETAILS
