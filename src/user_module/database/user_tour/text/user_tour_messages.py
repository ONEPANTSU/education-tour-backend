from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении связи user_tour"
get_all_success = "Успешное получение связи user_tour"

get_one_error = "Произошла ошибка при получении связи user_tour #{id}"
get_one_success = "Успешное получение связи user_tour #{id}"

create_error = "Произошла ошибка при создании связи user_tour"
create_success = "Успешное создание связи user_tour"

update_error = "Произошла ошибка при изменении связи user_tour #{id}"
update_success = "Успешное изменение связи user_tour #{id}"

delete_error = "Произошла ошибка при удалении связи user_tour #{id}"
delete_success = "Успешное удаление связи user_tour #{id}"


USER_TOUR_MESSAGE = {
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


class UserTourMessage(BaseMessage):
    _messages: dict = USER_TOUR_MESSAGE
