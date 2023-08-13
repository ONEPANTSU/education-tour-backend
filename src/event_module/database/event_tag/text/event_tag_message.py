from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении связи event_tag"
get_all_success = "Успешное получение связи event_tag"

get_one_error = "Произошла ошибка при получении связи event_tag #{id}"
get_one_success = "Успешное получение связи event_tag #{id}"

create_error = "Произошла ошибка при создании связи event_tag"
create_success = "Успешное создание связи event_tag"

update_error = "Произошла ошибка при изменении связи event_tag #{id}"
update_success = "Успешное изменение связи event_tag #{id}"

delete_error = "Произошла ошибка при удалении связи event_tag #{id}"
delete_success = "Успешное удаление связи event_tag #{id}"

get_by_event_id_error = ""
get_by_event_id_success = ""

EVENT_TAG_MESSAGE = {
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


class EventTagMessage(BaseMessage):
    _messages: dict = EVENT_TAG_MESSAGE
