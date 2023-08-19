from pydantic import BaseModel

from src.database_utils.base_models import BaseIDModel


class UserEventCreate(BaseModel):
    user_id: int
    event_id: int


class UserEventRead(BaseIDModel):
    user_id: int
    event_id: int


class UserEventDelete(BaseModel):
    user_id: int
    event_id: int


class UserEventUpdate(BaseIDModel):
    user_id: int
    event_id: int


class UserTourCreate(BaseModel):
    user_id: int
    tour_id: int


class UserTourRead(BaseIDModel):
    user_id: int
    tour_id: int


class UserTourUpdate(BaseIDModel):
    user_id: int
    tour_id: int


class UserTourDelete(BaseModel):
    user_id: int
    tour_id: int


class EventListRead(BaseModel):
    event_id_list: list[int] = []

    def set_by_user_event_read(self, user_event_read_list: list[UserEventRead]) -> None:
        for user_event in user_event_read_list:
            self.event_id_list.append(user_event.event_id)


class UserListRead(BaseModel):
    user_id_list: list[int] = []

    def set_by_user_event_read(self, user_event_read_list: list[UserEventRead]) -> None:
        for user_event in user_event_read_list:
            self.user_id_list.append(user_event.user_id)

    def set_by_user_tour_read(self, user_tour_read_list: list[UserTourRead]) -> None:
        for user_tour in user_tour_read_list:
            self.user_id_list.append(user_tour.user_id)


class TourListRead(BaseModel):
    tour_id_list: list[int] = []

    def set_by_user_tour_read(self, user_tour_read_list: list[UserTourRead]) -> None:
        for user_tour in user_tour_read_list:
            self.tour_id_list.append(user_tour.tour_id)
