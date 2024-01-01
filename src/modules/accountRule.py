from .base import Base
import sqlalchemy
import sqlalchemy.orm


class AccountRule(Base):
    __tablename__ = "AccountRule"

    __id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    __withdraw_fee = sqlalchemy.Column(
        "WithdrawFee",
        sqlalchemy.Float,
        nullable=False,
    )
    __minimum_initial_balance = sqlalchemy.Column(
        "MinimumInitialBalance",
        sqlalchemy.Float,
        nullable=False,
    )

    def __init__(
        self,
        withdraw_fee: float,
        minimum_initial_balance: float,
    ) -> None:
        self.__withdraw_fee = withdraw_fee
        self.__minimum_initial_balance = minimum_initial_balance

    def getId(self) -> str:
        return self.__id
