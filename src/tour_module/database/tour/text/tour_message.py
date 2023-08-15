from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении туров"
get_all_success = "Успешное получение туров"

get_one_error = "Произошла ошибка при получении тура #{id}"
get_one_success = "Успешное получение тура #{id}"

create_error = "Произошла ошибка при создании тура"
create_success = "Успешное создание тура"

update_error = "Произошла ошибка при изменении тура #{id}"
update_success = "Успешное изменение тура #{id}"

delete_error = "Произошла ошибка при удалении тура #{id}"
delete_success = "Успешное удаление тура #{id}"

TOUR_MESSAGE = {
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


class TourMessage(BaseMessage):
    _messages: dict = TOUR_MESSAGE
