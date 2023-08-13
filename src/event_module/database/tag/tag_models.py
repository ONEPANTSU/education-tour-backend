from src.database_utils.base_models import BaseModels
from src.event_module.models import Tag
from src.event_module.schemas import TagCreate, TagRead, TagUpdate


class TagModels(BaseModels):
    create_class: type = TagCreate
    update_class: type = TagUpdate
    read_class: type = TagRead
    database_table: type = Tag
