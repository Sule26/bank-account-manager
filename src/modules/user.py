from .base import Base
from datetime import datetime
import sqlalchemy
import sqlalchemy.orm


class User(Base):
    __tablename__ = "User"

    user_id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    first_name = sqlalchemy.Column(
        "FirstName",
        sqlalchemy.String,
        nullable=False,
    )
    last_name = sqlalchemy.Column(
        "LastName",
        sqlalchemy.String,
        nullable=False,
    )
    cpf = sqlalchemy.Column(
        "CPF",
        sqlalchemy.Integer,
        nullable=True,
    )
    username = sqlalchemy.Column(
        "Username",
        sqlalchemy.String,
        nullable=True,
    )
    password = sqlalchemy.Column(
        "Password",
        sqlalchemy.String,
        nullable=True,
    )
    email = sqlalchemy.Column(
        "Email",
        sqlalchemy.String,
        nullable=True,
    )
    phone = sqlalchemy.Column(
        "Phone",
        sqlalchemy.Integer,
        nullable=True,
    )
    birth_date = sqlalchemy.Column(
        "BirthDate",
        sqlalchemy.Date,
        nullable=False,
    )
    creation_date = sqlalchemy.Column(
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
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.creation_date: str = datetime.today().strftime("%Y-%m-%d")

    def __repr__(self) -> str:
        return f"""
        ({self.user_id})
        Name: {self.first_name} {self.last_name}
        CPF: {self.cpf}
        Email: {self.email}
        Phone: {self.phone}
        Born at: {self.birth_date}
        User created at: {self.creation_date}
        """
