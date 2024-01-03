from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Bank(Base):
    __tablename__ = "Bank"

    __id: Mapped[uuid.UUID] = mapped_column(
        name="id",
        primary_key=True,
        default=uuid.uuid4,
    )

    __name: Mapped[str] = mapped_column(
        String(64),
        name="name",
        nullable=False,
    )

    def __init__(
        self,
        name: str,
    ) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def getId(self) -> str:
        return self.__id
