from uuid import uuid4 as uuid
import sqlite3


class BankDatabase:

    def __init__(self) -> None:
        try:
            self.create_user_table()
            self.create_account_table()
            self.create_login_table()
            self.create_bank_table()
            self.create_accountuser_table()
            self.create_loginaccount_table()
            self.create_banklogin_table()
            self.insert_bank("Sule's Bank")
            self.insert_bank("Russel's Bank")
        except:
            pass

    # USER TABLE
    def create_user_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE user(
            cpf VARCHAR(15) NOT NULL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_user(self, cpf: str, first_name: str, last_name: str, age: int) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO user VALUES (:cpf, :f_name, :l_name, :age)", {"cpf": cpf, "f_name": first_name, "l_name": last_name, "age": age})
        conn.commit()
        conn.close()

    # ACCOUNT TABLE
    def create_account_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE account(
            idAccount TEXT PRIMARY KEY NOT NULL,
            balance MONEY NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_account(self, balance: float) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        self.new_idAccount = str(uuid())
        c.execute("INSERT INTO account VALUES (:idAccount, :balance)", {"idAccount": self.new_idAccount, "balance": balance})
        conn.commit()
        conn.close()

    # LOGIN TABLE
    def create_login_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE login(
            idLogin TEXT PRIMARY KEY NOT NULL,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_login(self, username: str, password: str) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        self.new_idLogin = str(uuid())
        c.execute("INSERT INTO login VALUES (:idLogin, :username, :password)", {"idLogin": self.new_idLogin, "username": username, "password": password})
        conn.commit()
        conn.close()

    # BANK TABLE
    def create_bank_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE bank(
            idBank TEXT PRIMARY KEY NOT NULL,
            name VARCHAR(25) NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_bank(self, name: str) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        self.new_idBank = str(uuid())
        c.execute("INSERT INTO bank VALUES (:idBank, :name)", {"idBank": self.new_idBank, "name": name})
        conn.commit()
        conn.close()

    # BANKLOGIN TABLE
    def create_banklogin_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE banklogin(
                idBank TEXT REFERENCES bank(idBank),
                idLogin TEXT REFERENCES login(idLogin)
            )""")
        conn.commit()
        conn.close()

    def insert_banklogin(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO banklogin VALUES (:idBank, :idLogin)", {"idBank": self.new_idBank, "idLogin": self.new_idLogin})
        conn.commit()
        conn.close()

    # LOGINACCOUNT TABLE
    def create_loginaccount_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE loginaccount(
            idLogin TEXT REFERENCES login(idLogin),
            idAccount TEXT REFERENCES account(idAccount)
        )""")
        conn.commit()
        conn.close()

    def insert_loginaccount(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO loginaccount VALUES (:idLogin, :idAccount)", {"idLogin": self.new_idLogin, "idAccount": self.new_idAccount})
        conn.commit()
        conn.close()

    # ACCOUNTUSER TABLE
    def create_accountuser_table(self) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE accountuser(
            cpf VARCHAR(15) REFERENCES user(cpf),
            idAccount TEXT REFERENCES account(idAccount)
        )""")
        conn.commit()
        conn.close()

    def insert_accountuser(self, cpf: str) -> None:
        conn = sqlite3.connect("src/database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO accountuser VALUES (:cpf, :idAccount)", {"cpf": cpf, "idAccount": self.new_idAccount})
        conn.commit()
        conn.close()
