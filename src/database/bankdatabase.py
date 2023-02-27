import sqlite3


class BankDatabase:

    def __init__(self) -> None:
        self.create_user_table()
        self.create_account_table()
        self.create_login_table()
        self.create_bank_table()

    # USER TABLE
    def create_user_table(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE user(
            cpf VARCHAR(15) NOT NULL PRIMARY KEY,
            first_name VARCHAR(25) NOT NULL,
            last_name VARCHAR(25) NOT NULL,
            age INTEGER NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_user(self, cpf: str, first_name: str, last_name: str, age: int) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO user VALUES (:cpf, :f_name, :l_name, :age)", {"cpf": cpf, "f_name": first_name, "l_name": last_name, "age": age})
        conn.commit()
        conn.close()

    # ACCOUNT TABLE
    def create_account_table(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE account(
            idAccount INTEGER PRIMARY KEY,
            balance MONEY NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_account(self, balance: float) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO account VALUES (null, :balance)", {"balance": balance})
        conn.commit()
        conn.close()

    # LOGIN TABLE
    def create_login_table(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE login(
            idLogin INTEGER PRIMARY KEY,
            username VARCHAR(25) NOT NULL,
            password VARCHAR(25) NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_login(self, username: str, password: str) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO login VALUES (null, :username, :password)", {"username": username, "password": password})
        conn.commit()
        conn.close()

    # BANK TABLE
    def create_bank_table(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE bank(
            idBank INTEGER PRIMARY KEY,
            name VARCHAR(25) NOT NULL
        )""")
        conn.commit()
        conn.close()

    def insert_bank(self, name: str) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()
        c.execute("INSERT INTO bank VALUES (null, :name)", {"name": name})
        conn.commit()
        conn.close()

    # BANKLOGIN TABLE
    def create_banklogin_table(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE banklogin(
                idBank INTEGER REFERENCES bank(idBank),
                idLogin INTEGER REFERENCES login(idLogin)
            )""")
        conn.commit()
        conn.close()

    def insert_banklogin(self) -> None:
        conn = sqlite3.connect("database/bank_database.db")
        c = conn.cursor()

        c.execute("INSERT INTO banklogin VALUES (null, null)")
        conn.commit()
        conn.close()
