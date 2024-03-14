from random import randint

from faker import Faker
from loguru import logger
from sqlalchemy import create_engine, or_, select
from sqlalchemy.orm import sessionmaker

from .account import Account
from .accountRule import AccountRule
from .accountType import ACCOUNT_TYPES, AccountType
from .bank import BANK_NAMES, Bank
from .base import Base
from .uris import MYSQL_URI, POSTGRES_URI
from .user import User

engine = create_engine(url=POSTGRES_URI)

# TODO: Solve the issues related to MySQL Syntax
# engine = sqlalchemy.create_engine(url=MYSQL_URI)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

check_banks = select(Bank).where(
    or_(
        Bank.name == BANK_NAMES["ITAU"],
        Bank.name == BANK_NAMES["SANTANDER"],
    )
)
check_banks_row = session.execute(check_banks).scalars().all()

if not check_banks_row:
    # Creating Banks
    itauBank = Bank(
        name=BANK_NAMES["ITAU"],
        account_types=[
            AccountType(
                name=ACCOUNT_TYPES["CHECKING"],
                account_rules=AccountRule(
                    withdraw_fee=1,
                    minimum_initial_balance=50,
                ),
            ),
            AccountType(
                name=ACCOUNT_TYPES["SAVING"],
                account_rules=AccountRule(
                    withdraw_fee=3,
                    minimum_initial_balance=200,
                ),
            ),
        ],
    )

    santanderBank = Bank(
        name=BANK_NAMES["SANTANDER"],
        account_types=[
            AccountType(
                name=ACCOUNT_TYPES["CHECKING"],
                account_rules=AccountRule(
                    withdraw_fee=1.5,
                    minimum_initial_balance=65,
                ),
            ),
            AccountType(
                name=ACCOUNT_TYPES["SAVING"],
                account_rules=AccountRule(
                    withdraw_fee=3.75,
                    minimum_initial_balance=175,
                ),
            ),
        ],
    )

    # Adding Banks to the database
    session.add_all(
        [
            itauBank,
            santanderBank,
        ]
    )

    session.commit()

fake_br = Faker(locale="pt_BR")
fake_gen = Faker()

stmt = select(AccountType).join(Bank)

account_type_rows = session.execute(stmt).scalars().all()

users = []
for index in range(0, 20):
    random_account_type = (account_type_rows[randint(0, 3)],)[0]
    users.append(
        User(
            first_name=fake_br.first_name(),
            last_name=fake_br.last_name(),
            cpf=fake_br.cpf(),
            username="username123",
            password="password123",
            email=fake_gen.email(),
            phone=fake_br.cellphone_number(),
            birth_date=fake_gen.date_of_birth(),
            accounts=[
                Account(
                    number=fake_gen.swift11(),
                    bank_id=random_account_type.bank_id,
                    account_type_id=random_account_type.id,
                    balance=randint(100, 100_000),
                ),
            ],
        )
    )

session.add_all(users)

session.commit()
