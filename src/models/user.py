import uuid
from datetime import date, datetime
from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .account import Account
from .base import Base


class User(Base):
    __tablename__ = "User"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    first_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    cpf: Mapped[str] = mapped_column(
        nullable=False,
        # unique=True,
    )
    username: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        # unique=True,
    )
    phone: Mapped[str] = mapped_column(
        nullable=False,
        # unique=True,
    )
    birth_date: Mapped[date] = mapped_column(
        nullable=False,
    )
    creation_date: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now().strftime("%Y-%m-%d %X"),
    )
    accounts: Mapped[List["Account"]] = relationship(
        back_populates="user",
    )

    def __repr__(self) -> str:
        return f"<User(first_name={self.first_name} last_name={self.last_name} cpf={self.cpf} username={self.username} password={self.password} email={self.email} phone={self.phone} birth_date={self.birth_date} creation_date={self.creation_date})>"
