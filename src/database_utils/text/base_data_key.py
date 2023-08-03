count = "count"
schemas = "schemas"
schema = "schema"

BASE_DATA_KEY = {
    "count": count,
    "schemas": schemas,
    "schema": schema,
}


class BaseDataKey:
    _data_key: dict = BASE_DATA_KEY

    def get(self, key: str):
        if key in self._data_key.keys():
            return self._data_key[key]
        else:
            return "ERROR 500: Неверный ключ DataKey"
