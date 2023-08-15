from enum import Enum

from src.database_utils.base_models import BaseModels
from src.tour_module.models import TourEvent
from src.tour_module.schemas import (
    EventListRead,
    TourEventCreate,
    TourEventListCreate,
    TourEventListDelete,
    TourEventRead,
    TourEventUpdate,
)


class TourEventFilter(Enum):
    TOUR = "tour_id"
    EVENT = "event_id"


class TourEventModels(BaseModels):
    create_class: type = TourEventCreate
    update_class: type = TourEventUpdate
    read_class: type = TourEventRead
    create_list_class: type = TourEventListCreate
    read_event_list_class: type = EventListRead
    delete_list_class: type = TourEventListDelete
    database_table: type = TourEvent
