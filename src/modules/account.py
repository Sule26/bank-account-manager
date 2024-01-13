from .base import Base
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Account(Base):
    __tablename__ = "Account"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    bank_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(column="Bank.id", ondelete="CASCADE"),
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
        default=datetime.now,
    )
