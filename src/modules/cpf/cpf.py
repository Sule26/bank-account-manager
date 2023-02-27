import random
import string


class Cpf:

    def __init__(self):
        pass

    def generateCpf(self) -> str:
        new_cpf = random.choices(string.digits, k=9)
        self.addDigits(new_cpf)
        new_cpf_completed = ''.join(new_cpf)
        return new_cpf_completed

    def addDigits(self, list: list[str]) -> None:
        list.append(self.nextDigit(list))
        list.append(self.nextDigit(list))

    def nextDigit(self, current_numbers: list[str]) -> str:
        lenght = len(current_numbers) + 1
        new_list = []
        for number in current_numbers:
            new_list.append(int(number) * lenght)
            lenght -= 1
        rest = sum(new_list) % 11
        if rest < 2:
            return str(0)
        else:
            return str(11 - rest)

    def verifyCpf(self, cpf: str) -> bool:
        cpf_list = [letter for letter in cpf if '.' not in letter and '-' not in letter]
        cpf_to_test = cpf_list[:9]
        self.addDigits(cpf_to_test)
        if cpf_to_test == list(cpf_list):
            return True
        return False

    def formatCpf(self, cpf: str) -> str:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
