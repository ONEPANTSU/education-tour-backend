from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String

from src.database import Base, metadata
from src.event_module.models import Event


class Tour(Base):
    __tablename__ = "tour"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(JSON, nullable=True)
    description = Column(String, nullable=False)
    date_start = Column(TIMESTAMP, default=datetime.utcnow)
    date_end = Column(TIMESTAMP, default=datetime.utcnow)
    reg_deadline = Column(TIMESTAMP, default=datetime.utcnow)
    max_users = Column(Integer, nullable=True)


class TourEvent(Base):
    __tablename__ = "tour_event"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    tour_id = Column(Integer, ForeignKey(Tour.id), nullable=False)
    event_id = Column(Integer, ForeignKey(Event.id), nullable=False)
