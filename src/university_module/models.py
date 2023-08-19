from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String

from src.database import Base, metadata
from src.event_module.models import Event
from src.tour_module.models import Tour


class University(Base):
    __tablename__ = "university"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(JSON, nullable=True)
    description = Column(String, nullable=True)
    reg_date = Column(TIMESTAMP, default=datetime.utcnow)


class UniversityEvent(Base):
    __tablename__ = "university_event"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    university_id = Column(Integer, ForeignKey(University.id), nullable=False)
    event_id = Column(Integer, ForeignKey(Event.id), nullable=False)


class UniversityTour(Base):
    __tablename__ = "university_tour"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    university_id = Column(Integer, ForeignKey(University.id), nullable=False)
    tour_id = Column(Integer, ForeignKey(Tour.id), nullable=False)
