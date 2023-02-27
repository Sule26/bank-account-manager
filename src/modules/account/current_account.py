from account import Account
from user import User

WITHDRAWAL_LIMIT = 5000


class CurrentAccount(Account):

    def __init__(self, owner: User, initial_balance: float) -> None:
        super().__init__(owner, initial_balance)

    def withdrawal(self, value) -> None:
        self.__withdrawal(value, WITHDRAWAL_LIMIT)


Account.register(CurrentAccount)
