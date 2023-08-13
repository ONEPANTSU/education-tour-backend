from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении тегов"
get_all_success = "Успешное получение тегов"

get_one_error = "Произошла ошибка при получении тега #{id}"
get_one_success = "Успешное получение тега #{id}"

create_error = "Произошла ошибка при создании тега"
create_success = "Успешное создание тега"

update_error = "Произошла ошибка при изменении тега #{id}"
update_success = "Успешное изменение тега #{id}"

delete_error = "Произошла ошибка при удалении тега #{id}"
delete_success = "Успешное удаление тега #{id}"

TAG_MESSAGE = {
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
}


class TagMessage(BaseMessage):
    _messages: dict = TAG_MESSAGE
