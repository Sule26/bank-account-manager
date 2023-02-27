from user import User
from abc import ABC, abstractmethod


class Account(ABC):

    __id: str

    def __init__(self, owner: User, initial_balance: float) -> None:
        self.owner = owner
        self.__balance = initial_balance
        self.__id

    def get_id(self) -> int:
        return self.__id

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, value) -> None:
        self.__balance += value

    def showAccount(self) -> None:
        print(f"\nOwner's Full Name: {self.owner.get_first_name()} {self.owner.get_last_name()}")
        print(f"Owner's Age: {self.owner.get_age()}")
        print(f"Balance: US${self.get_balance()}")
        print(f"Account id: {self.get_id()}")

    def deposit(self, value: float) -> None:
        self.set_balance(value)
        print("Deposit submitted!")

    @abstractmethod
    def withdrawal(self, value: float) -> None:
        pass

    def __withdrawal(self, value: float, limit: float) -> None:
        if self.get_balance() > value and value < limit:
            self.set_balance(-value)
        elif limit > value:
            print(f'You can just withdraw US${limit:.2f} for day!')
        else:
            print("You don't have enough funds!")

    def transference(self, value: float, other_account: "Account") -> None:
        if self.get_balance() > value:
            self.set_balance(-value)
            other_account.set_balance(value)
            print("You don't have enough funds!")
