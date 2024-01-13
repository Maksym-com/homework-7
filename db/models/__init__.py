from typing import Any
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

# self.__class__.__name__ + "s"

class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls)->str:
        return str(cls.__name__).lower() + "s"


    id: Mapped[int] = mapped_column(primary_key=True)


from . student import Goods
from . group import Group

