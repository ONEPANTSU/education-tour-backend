from src.database_utils.base_models import BaseModels
from src.event_module.models import Category
from src.event_module.schemas import CategoryCreate, CategoryRead, CategoryUpdate


class CategoryModels(BaseModels):
    create_class: type = CategoryCreate
    update_class: type = CategoryUpdate
    read_class: type = CategoryRead
    database_table: type = Category
