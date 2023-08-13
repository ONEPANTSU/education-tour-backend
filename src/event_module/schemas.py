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


class TagRead(BaseIDModel):
    name: str


class TagUpdate(BaseIDModel):
    name: str


class EventTagCreate(BaseModel):
    event_id: int
    tag_id: int


class EventTagRead(BaseIDModel):
    event_id: int
    tag_id: int


class EventTagUpdate(BaseIDModel):
    event_id: int
    tag_id: int


class EventTagListCreate(BaseModel):
    event_id: int
    tag_list: list[int]

    def get_event_tag_create_list(self) -> list[EventTagCreate]:
        event_tag_list = []
        for tag_id in self.tag_list:
            event_tag_list.append(EventTagCreate(event_id=self.event_id, tag_id=tag_id))
        return event_tag_list


class TagListRead(BaseModel):
    tag_id_list: list[int] = []

    def set_by_event_tag_read(self, event_tag_read_list: list[EventTagRead]) -> None:
        for event_tag in event_tag_read_list:
            self.tag_id_list.append(event_tag.tag_id)


class EventListRead(BaseModel):
    event_id_list: list[int] = []

    def set_by_event_tag_read(self, event_tag_read_list: list[EventTagRead]) -> None:
        for event_tag in event_tag_read_list:
            self.event_id_list.append(event_tag.event_id)


class EventTagListDelete(BaseModel):
    event_id: int
    tag_list: list[int]
