from src.database_utils.text.base_details import BaseDetails

wrong_id = "Указан неверный id категории"
trying_to_delete_foreign_key = (
    "Попытка удалить используемый внешний ключ: категория #{category_id}"
)

CATEGORY_DETAILS = {
    "wrong_id": wrong_id,
    "trying_to_delete_foreign_key": trying_to_delete_foreign_key,
}


class CategoryDetails(BaseDetails):
    _details = CATEGORY_DETAILS
