from src.database_utils.text.base_message import BaseMessage

get_all_error = "Произошла ошибка при получении университетов"
get_all_success = "Успешное получение университетов"

get_one_error = "Произошла ошибка при получении университета #{id}"
get_one_success = "Успешное получение университета #{id}"

create_error = "Произошла ошибка при создании университета"
create_success = "Успешное создание университета"

update_error = "Произошла ошибка при изменении университета #{id}"
update_success = "Успешное изменение университета #{id}"

delete_error = "Произошла ошибка при удалении университета #{id}"
delete_success = "Успешное удаление университета #{id}"

image_error = "Произошла ошибка при изменении изображения для университета #{id}"
image_success = "Успешное изменение изображения для университета #{id}"

UNIVERSITY_MESSAGE = {
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


class UniversityMessage(BaseMessage):
    _messages: dict = UNIVERSITY_MESSAGE
