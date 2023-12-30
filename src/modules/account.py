from .base import Base
import sqlalchemy
import sqlalchemy.orm


class Account(Base):
    __tablename__ = "Account"

    account_id = sqlalchemy.Column("Id", sqlalchemy.Uuid, primary_key=True)
    bank_id = sqlalchemy.Column(
        "BankId",
        sqlalchemy.Uuid,
        sqlalchemy.ForeignKey("Bank.Id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id = sqlalchemy.Column(
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
        self.bank_id = bank_id
        self.user_id = user_id
        self.balance = balance
        self.creation_date = creation_date

    def __repr__(self) -> str:
        return f"""
        ({self.account_id})
        BankId: {self.bank_id}
        UserId: {self.user_id}
        Balance: {self.balance}
        Creation Date: {self.creation_date}
        """
