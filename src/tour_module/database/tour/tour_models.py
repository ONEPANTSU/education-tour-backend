from src.database_utils.base_models import BaseModels
from src.tour_module.models import Tour
from src.tour_module.schemas import TourCreate, TourRead, TourUpdate


class TourModels(BaseModels):
    create_class: type = TourCreate
    update_class: type = TourUpdate
    read_class: type = TourRead
    database_table: type = Tour
