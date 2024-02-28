import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .accountType import AccountType
from .base import Base


class AccountRule(Base):
    __tablename__ = "AccountRule"

    id: Mapped[uuid.UUID] = mapped_column(
        name="id",
        primary_key=True,
        default=uuid.uuid4,
    )
    withdraw_fee: Mapped[float] = mapped_column(
        name="withdraw_fee",
        nullable=False,
    )
    minimum_initial_balance: Mapped[float] = mapped_column(
        name="minimum_initial_balance",
        nullable=False,
    )

    account_type: Mapped["AccountType"] = relationship(
        back_populates="account_rules", single_parent=True
    )

    def __repr__(self) -> str:
        return f"<AccountRule(id={self.id} withdraw_fee={self.withdraw_fee} minimum_initial_balance={self.minimum_initial_balance})>"
