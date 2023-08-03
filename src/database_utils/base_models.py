from abc import ABC

from pydantic import BaseModel

from src.database import Base


class BaseIDModel(BaseModel):
    id: int


class BaseModels(ABC):
    create_class: type = BaseModel
    update_class: type = BaseIDModel
    read_class: type = BaseIDModel
    database_table: type = Base
