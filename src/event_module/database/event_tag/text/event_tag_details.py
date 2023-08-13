from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы event_tag"

EVENT_TAG_DETAILS = {
    "wrong_id": wrong_id,
}


class EventTagDetails(BaseDetails):
    _details = EVENT_TAG_DETAILS
