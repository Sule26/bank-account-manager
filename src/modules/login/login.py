from account import Account


class Login:

    __id: str

    def __init__(self, username: str, password: str, account: Account):
        self.username = username
        self.password = password
        self.account = account
        self.__id

    def change_password(self, new_password: str) -> None:
        if len(new_password) > 5 and new_password != self.password:
            self.password = new_password
        else:
            print('Password not accepted!')
