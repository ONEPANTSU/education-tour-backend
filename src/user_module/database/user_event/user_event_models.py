from enum import Enum

from src.database_utils.base_models import BaseModels
from src.user_module.models import UserEvent
from src.user_module.schemas import (
    EventListRead,
    UserEventCreate,
    UserEventDelete,
    UserEventRead,
    UserEventUpdate,
    UserListRead,
)


class UserEventFilter(Enum):
    USER = "user_id"
    EVENT = "event_id"


class UserEventModels(BaseModels):
    create_class: type = UserEventCreate
    update_class: type = UserEventUpdate
    read_class: type = UserEventRead
    delete_class: type = UserEventDelete
    database_table: type = UserEvent

    read_user_list_class: type = UserListRead
    read_event_list_class: type = EventListRead
