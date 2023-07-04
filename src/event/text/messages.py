from templates.text.messages import MESSAGE_TEMPLATE

MESSAGE = {
    "get_all_events_error": MESSAGE_TEMPLATE["get_error"].format(object="мероприятий"),
    "get_all_events_success": MESSAGE_TEMPLATE["get_success"].format(
        object="мероприятий"
    ),
    "get_one_event_error": MESSAGE_TEMPLATE["get_error"].format(
        object="мероприятия #{event_id}"
    ),
    "get_one_event_success": MESSAGE_TEMPLATE["get_success"].format(
        object="мероприятия #{event_id}"
    ),
    "create_event_error": MESSAGE_TEMPLATE["create_error"].format(object="мероприятия"),
    "create_event_success": MESSAGE_TEMPLATE["create_success"].format(
        object="мероприятия"
    ),
    "update_event_error": MESSAGE_TEMPLATE["update_error"].format(
        object="мероприятия #{event_id}"
    ),
    "update_event_success": MESSAGE_TEMPLATE["update_success"].format(
        object="мероприятия #{event_id}"
    ),
    "delete_event_error": MESSAGE_TEMPLATE["delete_error"].format(
        object="мероприятия #{event_id}"
    ),
    "delete_event_success": MESSAGE_TEMPLATE["delete_success"].format(
        object="мероприятия #{event_id}"
    ),

    "get_all_categories_error": MESSAGE_TEMPLATE["get_error"].format(object="категорий"),
    "get_all_categories_success": MESSAGE_TEMPLATE["get_success"].format(
        object="категорий"
    ),
    "get_one_category_error": MESSAGE_TEMPLATE["get_error"].format(
        object="категории #{category_id}"
    ),
    "get_one_category_success": MESSAGE_TEMPLATE["get_success"].format(
        object="категории #{category_id}"
    ),
    "create_category_error": MESSAGE_TEMPLATE["create_error"].format(object="категории"),
    "create_category_success": MESSAGE_TEMPLATE["create_success"].format(
        object="категории"
    ),
    "update_category_error": MESSAGE_TEMPLATE["update_error"].format(
        object="категории #{category_id}"
    ),
    "update_category_success": MESSAGE_TEMPLATE["update_success"].format(
        object="категории #{category_id}"
    ),
    "delete_category_error": MESSAGE_TEMPLATE["delete_error"].format(
        object="категории #{category_id}"
    ),
    "delete_category_success": MESSAGE_TEMPLATE["delete_success"].format(
        object="категории #{category_id}"
    ),
}
