from sqlalchemy import Enum

from src.database_utils.base_models import BaseModels
from src.event_module.models import EventTag
from src.event_module.schemas import (
    EventListRead,
    EventTagCreate,
    EventTagListCreate,
    EventTagListDelete,
    EventTagRead,
    EventTagUpdate,
    TagListRead,
)


class EventTagFilter(Enum):
    EVENT = "event_id"
    TAG = "tag_id"


class EventTagModels(BaseModels):
    create_class: type = EventTagCreate
    update_class: type = EventTagUpdate
    read_class: type = EventTagRead

    create_list_class: type = EventTagListCreate
    read_tag_list_class: type = TagListRead
    read_event_list_class: type = EventListRead
    delete_list_class: type = EventTagListDelete

    database_table: type = EventTag
