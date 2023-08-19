from enum import Enum

from src.database_utils.base_models import BaseModels
from src.university_module.models import UniversityEvent
from src.university_module.schemas import (
    EventListRead,
    UniversityEventCreate,
    UniversityEventListCreate,
    UniversityEventListDelete,
    UniversityEventRead,
    UniversityEventUpdate,
)


class UniversityEventFilter(Enum):
    UNIVERSITY = "university_id"
    EVENT = "event_id"


class UniversityEventModels(BaseModels):
    create_class: type = UniversityEventCreate
    update_class: type = UniversityEventUpdate
    read_class: type = UniversityEventRead
    create_list_class: type = UniversityEventListCreate
    read_event_list_class: type = EventListRead
    delete_list_class: type = UniversityEventListDelete
    database_table: type = UniversityEvent
