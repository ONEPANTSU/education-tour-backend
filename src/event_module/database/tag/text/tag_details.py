from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан не верный id тега"

TAG_DETAILS = {"wrong_id": wrong_id}


class TagDetails(BaseDetails):
    _details = TAG_DETAILS
