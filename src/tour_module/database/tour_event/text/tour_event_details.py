from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы tour_event"

TOUR_EVENT_DETAILS = {
    "wrong_id": wrong_id,
}


class TourEventDetails(BaseDetails):
    _details = TOUR_EVENT_DETAILS
