import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from faker import Faker
from loguru import logger
from sqlalchemy import ForeignKey, create_engine, or_, select, update
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker

from .accountRule import AccountRule
from .accountType import AccountType
from .base import Base
from .uris import MYSQL_URI, POSTGRES_URI

if TYPE_CHECKING:
    from .user import User

engine = create_engine(url=POSTGRES_URI)
# TODO: Solve the issues related to MySQL Syntax
# engine = create_engine(url=MYSQL_URI)
Session = sessionmaker(bind=engine)
session = Session()


class Account(Base):
    __tablename__ = "Account"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    number: Mapped[str] = mapped_column(
        nullable=False,
        # unique=True,
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
    account_type: Mapped["AccountType"] = relationship(
        back_populates="account",
    )

    def __repr__(self) -> str:
        return f"<Account(id={self.id} bank_id={self.bank_id} account_type_id={self.account_type_id} user_id={self.user_id} balance={self.balance} creation_date={self.creation_date})>"

    def get_balance(self) -> float:
        return self.balance

    def set_balance(self, value: float) -> None:
        self.balance += value

    def update_database(self, account: "Account"):
        session.execute(
            update(Account)
            .where(Account.id == account.id)
            .values(balance=account.get_balance())
        )
        session.commit()

    def get_withdraw_fee(self) -> float:
        stmt = (
            select(AccountRule)
            .join(AccountType)
            .join(Account)
            .where(
                Account.account_type_id == AccountType.id,
                AccountType.account_rule_id == AccountRule.id,
            )
        )
        row = session.execute(stmt).scalars().first()
        return row.withdraw_fee

    def deposit(self, value: float) -> None:
        self.set_balance(value)
        self.update_database(self)
        logger.success("Deposit succeeded")

    def withdrawal(self, value: float) -> None:
        withdraw_fee = self.get_withdraw_fee()
        if not self.is_withdrawal_possible(value=value, withdraw_fee=withdraw_fee):
            logger.warning("You don't have enough money to withdraw!")
            return

        self.set_balance(-(value + withdraw_fee))
        self.update_database(self)
        logger.success("Withdrawal succeeded!")

    def is_withdrawal_possible(self, value: float, withdraw_fee: float) -> bool:
        if self.get_balance() < (value + withdraw_fee):
            return False
        return True

    def transference(self, value: float, receiver_account: "Account") -> None:
        if self.get_balance() < value:
            logger.warning("You don't have enough money to transfer!")
            return

        self.set_balance(-value)
        receiver_account.set_balance(value)
        self.update_database(self)
        self.update_database(receiver_account)
        logger.success("Transference succeeded!")
