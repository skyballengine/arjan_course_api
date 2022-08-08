
from enum import unique
from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from datetime import date

Base = declarative_base()

def to_dict(obj: Base) -> dict[str, Any]:
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

# added address_info, market_to columns
# added unique constraint to email_address 
class DBCustomer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False, unique=True)
    address_info = Column(String(250), nullable=False)
    market_to = Column(Boolean, nullable=False)

# added amenities column
# added unique constraint to number
class DBRoom(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(250), nullable=False, unique=True)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    amenities = Column(String(250), nullable=False)

# added cancel_able column
class DBBooking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship(DBCustomer)
    room_id = Column(Integer, ForeignKey("room.id"))
    room = relationship(DBRoom)
    price = Column(Integer, nullable=False)
    cancel_able = Column(Boolean, nullable=False)