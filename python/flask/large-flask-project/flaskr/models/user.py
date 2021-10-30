from sqlalchemy import UniqueConstraint, Column, ForeignKey
from sqlalchemy.types import Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column("id", UUID, primary_key=True)
    user_name = Column("name", String(120), unique=True, nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'))

    def __repr__(self):
        return f"{self.user_name}-{self.location_id}"
