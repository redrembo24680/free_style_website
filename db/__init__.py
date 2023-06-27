from .base import Base, session, engine
from .base import Base
from .models import Users

__all__ = [
    "Base",
    "Users"
]


def migrate():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


migrate()

