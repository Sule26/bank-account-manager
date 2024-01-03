from .base import Base
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Account(Base):
    __tablename__ = "Account"

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
    __user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="User.id", ondelete="CASCADE"),
        name="user_id",
        nullable=False,
    )
    __balance: Mapped[float] = mapped_column(
        name="balance",
        nullable=False,
    )
    __creation_date: Mapped[datetime] = mapped_column(
        name="creation_date",
        nullable=False,
        default=datetime.now,
    )

    # __id = sqlalchemy.Column(
    #     "Id",
    #     sqlalchemy.UUID(as_uuid=True),
    #     primary_key=True,
    #     default=uuid.uuid4,
    # )
    # __bank_id = sqlalchemy.Column(
    #     "BankId",
    #     sqlalchemy.Uuid,
    #     sqlalchemy.ForeignKey("Bank.Id", ondelete="CASCADE"),
    #     nullable=False,
    # )
    # __user_id = sqlalchemy.Column(
    #     "UserId",
    #     sqlalchemy.Uuid,
    #     sqlalchemy.ForeignKey("User.Id", ondelete="CASCADE"),
    #     nullable=False,
    # )

    # balance = sqlalchemy.Column("Balance", sqlalchemy.Float, nullable=False)
    # creation_date = sqlalchemy.Column("CreationDate", sqlalchemy.Date, nullable=False)

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
