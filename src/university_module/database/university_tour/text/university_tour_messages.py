from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении связи university_tour"
get_all_success = "Успешное получение связи university_tour"

get_one_error = "Произошла ошибка при получении связи university_tour #{id}"
get_one_success = "Успешное получение связи university_tour #{id}"

create_error = "Произошла ошибка при создании связи university_tour"
create_success = "Успешное создание связи university_tour"

update_error = "Произошла ошибка при изменении связи university_tour #{id}"
update_success = "Успешное изменение связи university_tour #{id}"

delete_error = "Произошла ошибка при удалении связи university_tour #{id}"
delete_success = "Успешное удаление связи university_tour #{id}"


UNIVERSITY_TOUR_MESSAGE = {
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


class UniversityTourMessage(BaseMessage):
    _messages: dict = UNIVERSITY_TOUR_MESSAGE
