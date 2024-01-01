from .base import Base
import sqlalchemy
import sqlalchemy.orm
import enum
import uuid


# class nameEnum(enum.Enum):
#     current_account = "Checking Account"
#     saving_account = "Saving_Account"


class AccountType(Base):
    __tablename__ = "AccountType"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    __bank_id = sqlalchemy.Column(
        "BankId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("Bank.Id", ondelete="CASCADE"),
        nullable=False,
    )

    __account_rule_id = sqlalchemy.Column(
        "AccountRuleId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("AccountRule.Id", ondelete="CASCADE"),
        nullable=False,
    )

    __name = sqlalchemy.Column(
        "Name",
        sqlalchemy.String,
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
