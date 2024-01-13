from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column


class Group(Base):
    """
    Related with Goods
    """
    name: Mapped[str]

    good: Mapped[str] = relationship('Goods', back_populates='group')
