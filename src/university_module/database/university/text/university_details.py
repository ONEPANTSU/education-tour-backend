from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан не верный id университета"

UNIVERSITY_DETAILS = {
    "wrong_id": wrong_id,
}


class UniversityDetails(BaseDetails):
    _details = UNIVERSITY_DETAILS
