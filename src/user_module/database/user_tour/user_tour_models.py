from enum import Enum

from src.database_utils.base_models import BaseModels
from src.user_module.models import UserTour
from src.user_module.schemas import (
    TourListRead,
    UserListRead,
    UserTourCreate,
    UserTourDelete,
    UserTourRead,
    UserTourUpdate,
)


class UserTourFilter(Enum):
    USER = "user_id"
    TOUR = "tour_id"


class UserTourModels(BaseModels):
    create_class: type = UserTourCreate
    update_class: type = UserTourUpdate
    read_class: type = UserTourRead
    delete_class: type = UserTourDelete
    database_table: type = UserTour

    read_tour_list_class: type = TourListRead
    read_user_list_class: type = UserListRead
