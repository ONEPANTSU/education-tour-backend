from src.database_utils.base_models import BaseModels
from src.event_module.models import Event
from src.event_module.schemas import EventCreate, EventRead, EventUpdate


class EventModels(BaseModels):
    create_class: type = EventCreate
    update_class: type = EventUpdate
    read_class: type = EventRead
    database_table: type = Event
