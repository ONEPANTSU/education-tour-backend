from templates.text.deteils import DETAILS_TEMPLATE

DETAILS = {
    "wrong_category_id": DETAILS_TEMPLATE["wrong_id"].format(object="категории"),
    "wrong_event_id": DETAILS_TEMPLATE["wrong_id"].format(object="мероприятия"),
    "trying_to_delete_category_foreign_key": DETAILS_TEMPLATE["trying_to_delete_foreign_key"].format(object="категория #{category_id}")
}
