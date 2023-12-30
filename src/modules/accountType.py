from .base import Base
import sqlalchemy
import sqlalchemy.orm
import enum


class nameEnum(enum.Enum):
    current_account = "Current Account"
    saving_account = "Saving_Account"


class AccountType(Base):
    __tablename__ = "AccountType"

    account_type_id = sqlalchemy.Column("Id", sqlalchemy.Uuid, primary_key=True)
    bank_id = sqlalchemy.Column(
        "BankId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("Bank.Id", ondelete="CASCADE"),
        nullable=False,
    )

    account_rule_id = sqlalchemy.Column(
        "AccountRuleId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("AccountRule.Id", ondelete="CASCADE"),
        nullable=False,
    )

    name = sqlalchemy.Column("Name", sqlalchemy.Enum(nameEnum), nullable=False)

    def __init__(
        self,
        bank_id: str,
        account_rule_id: str,
        name: str,
    ) -> None:
        self.bank_id = bank_id
        self.account_rule_id = account_rule_id
        self.name = name

    def __repr__(self) -> str:
        return f"""
        ({self.account_type_id})
        BankId: {self.bank_id}
        AccountRuleId: {self.account_rule_id}
        Name: {self.name}
        """
