from sqlalchemy import UniqueConstraint, Column
from sqlalchemy.types import Integer, String, Float
from sqlalchemy.orm import relationship

from .base import Base


class Location(Base):
    __tablename__ = 'location'
    id = Column("id", Integer(), primary_key=True, autoincrement=False, )
    name = Column("name", String(200), unique=True)
    lat = Column("lat", Float)
    long = Column("long", Float)
    UniqueConstraint(name, lat, long)
    users = relationship("User", backref="location")

    def __repr__(self):
        return f"Name:{self.name}lat/long:{self.lat}/{self.long}"
