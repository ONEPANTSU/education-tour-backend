from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан не верный id мероприятия"
wrong_category_id = "Указан не верный id категории"

EVENT_DETAILS = {
    "wrong_id": wrong_id,
    "wrong_category_id": wrong_category_id,
}


class EventDetails(BaseDetails):
    _details = EVENT_DETAILS
