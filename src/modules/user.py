from .base import Base
from datetime import datetime
import sqlalchemy
import sqlalchemy.orm
import uuid


class User(Base):
    __tablename__ = "User"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    __first_name = sqlalchemy.Column(
        "FirstName",
        sqlalchemy.String(25),
        nullable=False,
    )
    __last_name = sqlalchemy.Column(
        "LastName",
        sqlalchemy.String(25),
        nullable=False,
    )
    __cpf = sqlalchemy.Column(
        "CPF",
        sqlalchemy.Integer,
        nullable=True,
    )
    __username = sqlalchemy.Column(
        "Username",
        sqlalchemy.String(25),
        nullable=True,
    )
    __password = sqlalchemy.Column(
        "Password",
        sqlalchemy.String(25),
        nullable=True,
    )
    __email = sqlalchemy.Column(
        "Email",
        sqlalchemy.String(100),
        nullable=True,
    )
    __phone = sqlalchemy.Column(
        "Phone",
        sqlalchemy.Integer,
        nullable=True,
    )
    __birth_date = sqlalchemy.Column(
        "BirthDate",
        sqlalchemy.Date,
        nullable=False,
    )
    __creation_date = sqlalchemy.Column(
        "CreationDate",
        sqlalchemy.Date,
        nullable=False,
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
