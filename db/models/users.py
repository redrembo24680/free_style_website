from sqlalchemy import Column, Integer, BigInteger, Unicode, Float, Interval,Date

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
    ref_country_id = Column(
        Integer,
        unique=False,
        nullable=True
    )









