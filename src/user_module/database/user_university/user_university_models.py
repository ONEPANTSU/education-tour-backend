from enum import Enum

from src.database_utils.base_models import BaseModels
from src.user_module.models import UserUniversity
from src.user_module.schemas import (
    UserUniversityCreate,
    UserUniversityUpdate,
    UserUniversityRead,
    UserUniversityDelete,
)


class UserUniversityFilter(Enum):
    USER = "user_id"
    UNIVERSITY = "university_id"


class UserUniversityModels(BaseModels):
    create_class: type = UserUniversityCreate
    update_class: type = UserUniversityUpdate
    read_class: type = UserUniversityRead
    delete_class: type = UserUniversityDelete
    database_table: type = UserUniversity
