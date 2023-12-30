from cpf import Cpf


class User:
    cpf_object = Cpf()

    def __init__(self, first_name: str, last_name: str, age: int, cpf: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__CPF = self.cpf_object.formatCpf(cpf)

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_age(self) -> int:
        return self.__age

    def get_CPF(self) -> str:
        return self.__CPF
