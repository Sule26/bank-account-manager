from .base import Base
import sqlalchemy
import sqlalchemy.orm


class Account(Base):
    __tablename__ = "Account"

    __id = sqlalchemy.Column(
    __bank_id = sqlalchemy.Column(
        "BankId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("Bank.Id", ondelete="CASCADE"),
        nullable=False,
    )
    __user_id = sqlalchemy.Column(
        "UserId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("User.Id", ondelete="CASCADE"),
        nullable=False,
    )

    balance = sqlalchemy.Column("Balance", sqlalchemy.Float, nullable=False)
    creation_date = sqlalchemy.Column("CreationDate", sqlalchemy.Date, nullable=False)

    def __init__(
        self,
        bank_id: str,
        user_id: str,
        balance: float,
        creation_date: str,
    ) -> None:
        self.__bank_id = bank_id
        self.__user_id = user_id
        self.__balance = balance
        self.__creation_date = creation_date

    def getId(self) -> str:
        return self.__id
