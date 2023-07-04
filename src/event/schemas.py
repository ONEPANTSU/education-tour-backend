from datetime import datetime

from loguru import logger
from pydantic import BaseModel


class EventCreate(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: str

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class EventRead(BaseModel):
    id: int
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: str


class EventUpdate(BaseModel):
    id: int
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: str

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class CategoryCreate(BaseModel):
    name: str


class CategoryRead(BaseModel):
    id: int
    name: str


class CategoryUpdate(BaseModel):
    id: int
    name: str
