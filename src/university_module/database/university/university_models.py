from src.database_utils.base_models import BaseModels
from src.university_module.models import University
from src.university_module.schemas import (
    UniversityCreate,
    UniversityRead,
    UniversityUpdate,
)


class UniversityModels(BaseModels):
    create_class: type = UniversityCreate
    update_class: type = UniversityUpdate
    read_class: type = UniversityRead
    database_table: type = University
