from .base import Base
import sqlalchemy
import sqlalchemy.orm
import uuid


class Bank(Base):
    __tablename__ = "Bank"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
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
