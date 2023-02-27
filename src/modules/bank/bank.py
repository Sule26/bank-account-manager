from login import Login


class Bank:
    __login_list: list[Login] = []
    __id: str

    def __init__(self, name: str) -> None:
        self.name = name
        self.__login_list: list[Login]
        self.__id

    def append(self, new_login: "Login") -> None:
        self.__login_list.append(new_login)

    def get_login_list(self) -> list[Login]:
        return self.__login_list
