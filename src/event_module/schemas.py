from datetime import datetime

from loguru import logger
from pydantic import BaseModel

from src.address_schema import Address
from src.database_utils.base_models import BaseIDModel


class EventCreate(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int = 1
    address: Address

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class EventRead(BaseIDModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: Address


class EventUpdate(BaseIDModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int = 1
    address: Address

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class CategoryCreate(BaseModel):
    name: str


class CategoryRead(BaseIDModel):
    name: str


class CategoryUpdate(BaseIDModel):
    name: str


class TagCreate(BaseModel):
    name: str


class TagRead(BaseModel):
    id: int
    name: str


class TagUpdate(BaseModel):
    id: int
    name: str
