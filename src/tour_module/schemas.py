from datetime import datetime

from loguru import logger
from pydantic import BaseModel

from src.address_schema import Address
from src.database_utils.base_models import BaseIDModel


class TourCreate(BaseModel):
    name: str
    address: Address | None
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    image: str | None = None

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class TourRead(BaseIDModel):
    name: str
    address: Address | None
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    image: str | None


class TourUpdate(BaseIDModel):
    name: str
    address: Address | None
    description: str
    date_start: datetime
    date_end: datetime
    reg_deadline: datetime
    max_users: int
    image: str | None

    @logger.catch
    def fix_time(self) -> None:
        self.date_start = self.date_start.replace(tzinfo=None)
        self.date_end = self.date_end.replace(tzinfo=None)
        self.reg_deadline = self.reg_deadline.replace(tzinfo=None)


class TourEventCreate(BaseModel):
    tour_id: int
    event_id: int


class TourEventRead(BaseIDModel):
    tour_id: int
    event_id: int


class TourEventUpdate(BaseIDModel):
    tour_id: int
    event_id: int


class TourEventListCreate(BaseModel):
    tour_id: int
    event_list: list[int]

    def get_tour_event_create_list(self) -> list[TourEventCreate]:
        tour_event_list = []
        for event_id in self.event_list:
            tour_event_list.append(
                TourEventCreate(tour_id=self.tour_id, event_id=event_id)
            )
        return tour_event_list


class EventListRead(BaseModel):
    event_id_list: list[int] = []

    def set_by_tour_event_read(self, tour_event_read_list: list[TourEventRead]) -> None:
        for tour_event in tour_event_read_list:
            self.event_id_list.append(tour_event.event_id)


class TourEventListDelete(BaseModel):
    tour_id: int
    event_list: list[int]
