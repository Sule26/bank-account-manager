from .base import Base
import sqlalchemy
import sqlalchemy.orm


class AccountRule(Base):
    __tablename__ = "AccountRule"

    account_rule_id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    withdraw_fee = sqlalchemy.Column(
        "WithdrawFee",
        sqlalchemy.Float,
        nullable=False,
    )
    minimum_initial_balance = sqlalchemy.Column(
        "MinimumInitialBalance",
        sqlalchemy.Float,
        nullable=False,
    )

    def __init__(
        self,
        withdraw_fee: float,
        minimum_initial_balance: float,
    ) -> None:
        self.withdraw_fee = withdraw_fee
        self.minimum_initial_balance = minimum_initial_balance

    def __repr__(self) -> str:
        return f"""
        ({self.account_rule_id}) 
        withdraw Fee: {self.withdraw_fee}
        Minimum Initial Balance: {self.minimum_initial_balance}
        """
