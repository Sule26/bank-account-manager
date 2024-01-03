from .base import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
import uuid


# class nameEnum(enum.Enum):
#     current_account = "Checking Account"
#     saving_account = "Saving_Account"


class AccountType(Base):
    __tablename__ = "AccountType"

    __id: Mapped[uuid.UUID] = mapped_column(
        name="id",
        primary_key=True,
        default=uuid.uuid4,
    )

    __bank_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="Bank.id", ondelete="CASCADE"),
        name="bank_id",
        nullable=False,
    )

    __account_rule_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="AccountRule.id", ondelete="CASCADE"),
        name="account_rule_id",
        nullable=False,
    )

    __name: Mapped[str] = mapped_column(
        String(64),
        name="name",
        nullable=False,
    )

    def __init__(
        self,
        bank_id: str,
        account_rule_id: str,
        name: str,
    ) -> None:
        self.__bank_id = bank_id
        self.__account_rule_id = account_rule_id
        self.__name = name

    def getId(self) -> str:
        return self.__id
