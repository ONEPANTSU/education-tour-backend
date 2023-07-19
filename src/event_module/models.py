from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String

from src.database import Base, metadata


class Category(Base):
    __tablename__ = "category"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Event(Base):
    __tablename__ = "event"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_start = Column(TIMESTAMP, default=datetime.utcnow)
    date_end = Column(TIMESTAMP, default=datetime.utcnow)
    reg_deadline = Column(TIMESTAMP, default=datetime.utcnow)
    max_users = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    address = Column(JSON, nullable=True)
