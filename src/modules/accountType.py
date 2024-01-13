import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .accountRule import AccountRule
    from .bank import Bank


class AccountType(Base):
    __tablename__ = "AccountType"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    bank_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="Bank.id", ondelete="CASCADE"),
        nullable=False,
    )

    account_rule_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="AccountRule.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    
