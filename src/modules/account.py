import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Account(Base):
    __tablename__ = "Account"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    bank_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="Bank.id", ondelete="CASCADE"),
        nullable=False,
    )
    account_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="AccountType.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="User.id", ondelete="CASCADE"),
        nullable=False,
    )
    balance: Mapped[float] = mapped_column(
        nullable=False,
    )
    creation_date: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now().strftime("%Y-%m-%d %X"),
    )
    user: Mapped["User"] = relationship(
        back_populates="accounts",
    )

    def __repr__(self) -> str:
        return f"<Account(id={self.id} bank_id={self.bank_id} account_type_id={self.account_type_id} user_id={self.user_id} balance={self.balance} creation_date={self.creation_date})>"
