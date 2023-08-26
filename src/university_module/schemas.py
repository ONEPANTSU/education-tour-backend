from datetime import datetime

from loguru import logger
from pydantic import BaseModel

from src.address_schema import Address
from src.database_utils.base_models import BaseIDModel


class UniversityCreate(BaseModel):
    name: str
    url: str
    phone: str
    email: str
    address: Address
    description: str
    reg_date: datetime
    image: str | None = None

    @logger.catch
    def fix_time(self) -> None:
        self.reg_date = self.reg_date.replace(tzinfo=None)


class UniversityRead(BaseIDModel):
    name: str
    url: str
    phone: str
    email: str
    address: Address
    description: str
    reg_date: datetime
    image: str | None


class UniversityUpdate(BaseIDModel):
    name: str
    url: str
    phone: str
    email: str
    address: Address
    description: str
    reg_date: datetime
    image: str | None

    @logger.catch
    def fix_time(self) -> None:
        self.reg_date = self.reg_date.replace(tzinfo=None)


class UniversityEventCreate(BaseModel):
    university_id: int
    event_id: int


class UniversityEventRead(BaseIDModel):
    university_id: int
    event_id: int


class UniversityEventUpdate(BaseIDModel):
    university_id: int
    event_id: int


class UniversityEventListCreate(BaseModel):
    university_id: int
    event_list: list[int]

    def get_university_event_create_list(self) -> list[UniversityEventCreate]:
        university_event_list = []
        for event_id in self.event_list:
            university_event_list.append(
                UniversityEventCreate(
                    university_id=self.university_id, event_id=event_id
                )
            )
        return university_event_list


class EventListRead(BaseModel):
    event_id_list: list[int] = []

    def set_by_university_event_read(
        self, university_event_read_list: list[UniversityEventRead]
    ) -> None:
        for university_event in university_event_read_list:
            self.event_id_list.append(university_event.event_id)


class UniversityEventListDelete(BaseModel):
    university_id: int
    event_list: list[int]


class UniversityTourCreate(BaseModel):
    university_id: int
    tour_id: int


class UniversityTourRead(BaseIDModel):
    university_id: int
    tour_id: int


class UniversityTourUpdate(BaseIDModel):
    university_id: int
    tour_id: int


class UniversityTourListCreate(BaseModel):
    university_id: int
    tour_list: list[int]

    def get_university_tour_create_list(self) -> list[UniversityTourCreate]:
        university_tour_list = []
        for tour_id in self.tour_list:
            university_tour_list.append(
                UniversityTourCreate(university_id=self.university_id, tour_id=tour_id)
            )
        return university_tour_list


class TourListRead(BaseModel):
    tour_id_list: list[int] = []

    def set_by_university_tour_read(
        self, university_tour_read_list: list[UniversityTourRead]
    ) -> None:
        for university_tour in university_tour_read_list:
            self.tour_id_list.append(university_tour.tour_id)


class UniversityTourListDelete(BaseModel):
    university_id: int
    tour_list: list[int]
