from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении связи tour_event"
get_all_success = "Успешное получение связи tour_event"

get_one_error = "Произошла ошибка при получении связи tour_event #{id}"
get_one_success = "Успешное получение связи tour_event #{id}"

create_error = "Произошла ошибка при создании связи tour_event"
create_success = "Успешное создание связи tour_event"

update_error = "Произошла ошибка при изменении связи tour_event #{id}"
update_success = "Успешное изменение связи tour_event #{id}"

delete_error = "Произошла ошибка при удалении связи tour_event #{id}"
delete_success = "Успешное удаление связи tour_event #{id}"


TOUR_EVENT_MESSAGE = {
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


class TourEventMessage(BaseMessage):
    _messages: dict = TOUR_EVENT_MESSAGE
