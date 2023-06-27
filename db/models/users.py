from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, Date, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from .country import *
from .orders import *

from .. import Base

__all__ = ['Base']


class Users(Base):
    __tablename__ = 'users'
    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    first_name = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    second_name = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    email = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )
    password = Column(
        Unicode(225),
        unique=False,
        nullable=False
    )
    date = Column(
        Date,
        unique=False,
        nullable=True
    )
    country = mapped_column(
        Integer,
        ForeignKey('countries.id'),
        unique=True,
        nullable=True
    )
    order = relationship('orders', backref="users")
