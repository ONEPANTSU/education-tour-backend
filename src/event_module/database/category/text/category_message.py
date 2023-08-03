from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении категорий"
get_all_success = "Успешное получение категорий"

get_one_error = "Произошла ошибка при получении категории #{id}"
get_one_success = "Успешное получение категории #{id}"

create_error = "Произошла ошибка при создании категории"
create_success = "Успешное создание категории"

update_error = "Произошла ошибка при изменении категории #{id}"
update_success = "Успешное изменение категории #{id}"

delete_error = "Произошла ошибка при удалении категории #{id}"
delete_success = "Успешное удаление категории #{id}"

CATEGORY_MESSAGE = {
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


class CategoryMessage(BaseMessage):
    _messages: dict = CATEGORY_MESSAGE
