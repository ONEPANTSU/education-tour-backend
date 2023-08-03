wrong_id = "Указан не верный id"

BASE_DETAILS = {
    "wrong_id": wrong_id,
}


class BaseDetails:
    _details: dict = BASE_DETAILS

    def get(self, details: str):
        if details in self._details.keys():
            return self._details[details]
        else:
            return "ERROR 500: Неверный ключ Details"
