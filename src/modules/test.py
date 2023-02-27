from bank.bank import Bank
from user.user import User
from login.login import Login
from cpf.cpf import Cpf
from account.current_account import CurrentAccount
from account.saving_account import SavingAccount

cpf = Cpf()
bank = Bank("Sule's Bank")

user1 = User('Sule', 'Russell', 22, cpf.generateCpf())
user2 = User('Daniel', 'Dietrich', 21, cpf.generateCpf())

current = CurrentAccount(user1, 10000)
saving = SavingAccount(user2, 50000)

login1 = Login('Sule26', 'Sule26', current)
login2 = Login('Sule25', 'Sule25', saving)

bank.append(login1)
bank.append(login2)

list = bank.get_login_list()
print(list[1].account.owner.get_CPF())

# current.showAccount()
# print(current.owner.get_CPF())

# saving.showAccount()
# print(saving.owner.get_CPF())
