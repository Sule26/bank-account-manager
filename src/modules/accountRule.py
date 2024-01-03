from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class AccountRule(Base):
    __tablename__ = "AccountRule"

    __id: Mapped[uuid.UUID] = mapped_column(
        name="id",
        primary_key=True,
        default=uuid.uuid4,
    )
    __withdraw_fee: Mapped[float] = mapped_column(
        name="withdraw_fee",
        nullable=False,
    )
    __minimum_initial_balance: Mapped[float] = mapped_column(
        name="minimum_initial_balance",
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
