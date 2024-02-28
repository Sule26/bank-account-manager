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
    )
    phone: Mapped[str] = mapped_column(
        nullable=False,
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
