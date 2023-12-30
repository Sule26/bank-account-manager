from .base import Base
import sqlalchemy
import sqlalchemy.orm


class Bank(Base):
    __tablename__ = "Bank"

    bank_id = sqlalchemy.Column(
        "Id",
        sqlalchemy.Uuid,
        primary_key=True,
    )
    name = sqlalchemy.Column(
        "Name",
        sqlalchemy.Integer,
        nullable=False,
    )

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"({self.bank_id}) -> {self.name}"
