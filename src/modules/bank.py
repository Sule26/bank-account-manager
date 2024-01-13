import uuid
from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .accountType import AccountType
from .base import Base


class Bank(Base):
    __tablename__ = "Bank"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    account_types: Mapped[List["AccountType"]] = relationship(
        back_populates="bank",
    )
