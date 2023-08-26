from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении мероприятий"
get_all_success = "Успешное получение мероприятий"

get_by_category_error = (
    "Произошла ошибка при получении мероприятий по category_id #{id}"
)
get_by_category_success = "Успешное получение мероприятий по category_id #{id}"

get_one_error = "Произошла ошибка при получении мероприятия #{id}"
get_one_success = "Успешное получение мероприятия #{id}"

create_error = "Произошла ошибка при создании мероприятия"
create_success = "Успешное создание мероприятия"

update_error = "Произошла ошибка при изменении мероприятия #{id}"
update_success = "Успешное изменение мероприятия #{id}"

delete_error = "Произошла ошибка при удалении мероприятия #{id}"
delete_success = "Успешное удаление мероприятия #{id}"

image_error = "Произошла ошибка при изменении изображения для мероприятия #{id}"
image_success = "Успешное изменение изображения для мероприятия #{id}"

EVENT_MESSAGE = {
    "get_all_error": get_all_error,
    "get_all_success": get_all_success,
    "get_by_category_error": get_by_category_error,
    "get_by_category_success": get_by_category_success,
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


class EventMessage(BaseMessage):
    _messages: dict = EVENT_MESSAGE
