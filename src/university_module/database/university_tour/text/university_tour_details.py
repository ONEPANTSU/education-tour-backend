from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id таблицы university_tour"

UNIVERSITY_TOUR_DETAILS = {
    "wrong_id": wrong_id,
}


class UniversityTourDetails(BaseDetails):
    _details = UNIVERSITY_TOUR_DETAILS
