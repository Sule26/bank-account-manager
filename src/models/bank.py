import enum
import uuid
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .accountType import AccountType
from .base import Base

# Todo: Use Enum instead of str
# class BankEnum(enum.Enum):
#     ITAU = "Itaú"
#     SANTANDER = "Santander"


class Bank(Base):
    __tablename__ = "Bank"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    account_types: Mapped[List["AccountType"]] = relationship(
        back_populates="bank",
    )

    def __repr__(self) -> str:
        return f"<Bank(id={self.id} name={self.name})>"
