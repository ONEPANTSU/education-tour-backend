from sqlalchemy import Column, ForeignKey, Integer

from src.database import Base, metadata
from src.event_module.models import Event
from src.tour_module.models import Tour


class UserEvent(Base):
    __tablename__ = "user_event"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, ForeignKey(Event.id), nullable=False)


class UserTour(Base):
    __tablename__ = "user_tour"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    tour_id = Column(Integer, ForeignKey(Tour.id), nullable=False)
