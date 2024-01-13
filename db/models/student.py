from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column



class Goods(Base):
    """
    Related with Group
    """
    name: Mapped[str]
    type: Mapped[str]
    quantity: Mapped[int]
    deliveries: Mapped[int]
    sales: Mapped[int]
    customers: Mapped[int]
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    group: Mapped[str] = relationship('Group', back_populates='good')

