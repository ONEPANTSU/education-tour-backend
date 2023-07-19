import json
from datetime import datetime

from loguru import logger
from pydantic import BaseModel


class Address(BaseModel):
    country: str = None
    city: str = None
    street: str = None
    house: int = None
    corps: int = None
    building: int = None
    level: int = None
    flat: int = None
    office: int = None


class EventCreate(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: Address

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
    address: Address


class EventUpdate(BaseModel):
    id: int
    name: str
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    category_id: int
    address: Address

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
