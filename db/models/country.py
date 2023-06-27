from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval, ForeignKey
from sqlalchemy.orm import relationship
from .users import *

from .. import Base

__all__ = ['Base']


class Country(Base):
    __tablename__ = 'countries'
    id = Column(
        BigInteger,
        ForeignKey('users.country'),
        primary_key=True,
        autoincrement=True
    )
    title = Column(
        Unicode(225),
        unique=True,
        nullable=False
    )


