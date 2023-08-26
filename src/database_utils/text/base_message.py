get_all_error = "Произошла ошибка при получении"
get_all_success = "Успешное получение"

get_one_error = "Произошла ошибка при получении #{id}"
get_one_success = "Успешное получение #{id}"

create_error = "Произошла ошибка при создании"
create_success = "Успешное создание"

update_error = "Произошла ошибка при изменении #{id}"
update_success = "Успешное изменение #{event_id}"

delete_error = "Произошла ошибка при удалении #{id}"
delete_success = "Успешное удаление #{id}"

image_error = "Произошла ошибка при изменении изображения для #{id}"
image_success = "Успешное изменение изображения для #{id}"

BASE_MESSAGE = {
    "get_all_error": get_all_error,
    "get_all_success": get_all_success,
    "get_one_error": get_one_error,
    "get_one_success": get_one_success,
    "create_error": create_error,
    "create_success": create_success,
    "update_error": update_error,
    "update_success": update_success,
    "delete_error": delete_error,
    "delete_success": delete_success,
    "image_error": image_error,
    "image_success": image_success,
}


class BaseMessage:
    _messages: dict = BASE_MESSAGE

    def get(self, message: str):
        if message in self._messages.keys():
            return self._messages[message]
        else:
            return "ERROR 500: Неверный ключ Message"
