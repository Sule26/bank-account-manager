import enum
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .accountRule import AccountRule
    from .bank import Bank

# Todo: Use Enum instead of str
# class AccountTypeEnum(enum.Enum):
#     CHECKING_ACCOUNT = "Checking Account"
#     SAVING_ACCOUNT = "Saving Account"


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
        nullable=False,
    )

    bank: Mapped["Bank"] = relationship(
        back_populates="account_types",
    )

    account_rules: Mapped["AccountRule"] = relationship(
        back_populates="account_type",
    )

    def __repr__(self) -> str:
        return f"<AccountType(id={self.id} bank_id={self.bank_id} account_rule_id={self.account_rule_id} name={self.name}>"
