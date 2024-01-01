from .base import Base
from datetime import datetime
import sqlalchemy
import sqlalchemy.orm


class User(Base):
    __tablename__ = "User"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    __first_name = sqlalchemy.Column(
        "FirstName",
        sqlalchemy.String,
        nullable=False,
    )
    __last_name = sqlalchemy.Column(
        "LastName",
        sqlalchemy.String,
        nullable=False,
    )
    __cpf = sqlalchemy.Column(
        "CPF",
        sqlalchemy.Integer,
        nullable=True,
    )
    __username = sqlalchemy.Column(
        "Username",
        sqlalchemy.String,
        nullable=True,
    )
    __password = sqlalchemy.Column(
        "Password",
        sqlalchemy.String,
        nullable=True,
    )
    __email = sqlalchemy.Column(
        "Email",
        sqlalchemy.String,
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
