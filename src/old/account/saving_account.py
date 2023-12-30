from account import Account
from user import User

WITHDRAWAL_LIMIT = 1000


class SavingAccount(Account):

    def __init__(self, owner: User, initial_balance: float):
        super().__init__(owner, initial_balance)

    def withdrawal(self, value: float):
        self.__withdrawal(value, WITHDRAWAL_LIMIT)


Account.register(SavingAccount)
