from sqlalchemy import Enum

from src.database_utils.base_models import BaseModels
from src.university_module.models import UniversityTour
from src.university_module.schemas import (
    TourListRead,
    UniversityTourCreate,
    UniversityTourListCreate,
    UniversityTourListDelete,
    UniversityTourRead,
    UniversityTourUpdate,
)


class UniversityTourFilter(Enum):
    UNIVERSITY = "university_id"
    TOUR = "tour_id"


class UniversityTourModels(BaseModels):
    create_class: type = UniversityTourCreate
    update_class: type = UniversityTourUpdate
    read_class: type = UniversityTourRead
    create_list_class: type = UniversityTourListCreate
    read_tour_list_class: type = TourListRead
    delete_list_class: type = UniversityTourListDelete
    database_table: type = UniversityTour
