from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы user_tour"

USER_TOUR_DETAILS = {
    "wrong_id": wrong_id,
}


class UserTourDetails(BaseDetails):
    _details = USER_TOUR_DETAILS
