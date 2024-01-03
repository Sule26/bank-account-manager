from .base import Base
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class User(Base):
    __tablename__ = "User"

    __id: Mapped[uuid.UUID] = mapped_column(
        name="id",
        primary_key=True,
        default=uuid.uuid4,
    )

    __first_name: Mapped[str] = mapped_column(
        String(64),
        name="first_name",
        nullable=False,
    )
    __last_name: Mapped[str] = mapped_column(
        String(64),
        name="last_name",
        nullable=False,
    )
    __cpf: Mapped[int] = mapped_column(
        name="cpf",
        nullable=False,
    )
    __username: Mapped[str] = mapped_column(
        String(64),
        name="username",
        nullable=False,
    )
    __password: Mapped[str] = mapped_column(
        String(64),
        name="password",
        nullable=False,
    )
    __email: Mapped[str] = mapped_column(
        String(120),
        name="email",
        nullable=False,
    )
    __phone: Mapped[int] = mapped_column(
        name="phone",
        nullable=False,
    )
    __birth_date: Mapped[datetime] = mapped_column(
        name="birth_date",
        nullable=False,
    )
    __creation_date: Mapped[datetime] = mapped_column(
        name="creation_date",
        nullable=False,
        default=datetime.now,
    )

    def __init__(
        self,
        first_name: str,
        last_name: str,
        cpf: int,
        username: str,
        password: str,
        email: str,
        phone: int,
        birth_date: str,
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cpf = cpf
        self.__username = username
        self.__password = password
        self.__email = email
        self.__phone = phone
        self.__birth_date = birth_date
        self.__creation_date: str = datetime.today().strftime("%Y-%m-%d")
