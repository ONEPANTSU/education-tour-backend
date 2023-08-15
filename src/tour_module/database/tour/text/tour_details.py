from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан не верный id тура"
wrong_event_id = "Указан не верный id мероприятия"

TOUR_DETAILS = {
    "wrong_id": wrong_id,
    "wrong_event_id": wrong_event_id,
}


class TourDetails(BaseDetails):
    _details = TOUR_DETAILS
