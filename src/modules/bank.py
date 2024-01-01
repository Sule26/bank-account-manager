from .base import Base
import sqlalchemy
import sqlalchemy.orm


class Bank(Base):
    __tablename__ = "Bank"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    __name = sqlalchemy.Column(
        "Name",
        sqlalchemy.String,
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
