from .base import Base
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import uuid


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
    cpf: Mapped[int] = mapped_column(
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
    phone: Mapped[int] = mapped_column(
        nullable=False,
    )
    birth_date: Mapped[datetime] = mapped_column(
        nullable=False,
    )
    _reation_date: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now,
    )
