import sqlalchemy.orm
from loguru import logger

from .account import Account
from .accountRule import AccountRule
from .accountType import AccountType
from .bank import Bank
from .base import Base
from .uris import MYSQL_URI, POSTGRES_URI
from .user import User

ACCOUNT_TYPES = ["Checking Account", "Saving Account"]

engine = sqlalchemy.create_engine(url=POSTGRES_URI)

# TODO: Solve the issues related to MySQL Syntax
# engine = sqlalchemy.create_engine(url=MYSQL_URI)

Base.metadata.create_all(bind=engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# Creating Banks
itauBank = Bank(
    name="Itaú",
    account_types=[
        AccountType(
            name=ACCOUNT_TYPES[0],
            account_rules=AccountRule(
                withdraw_fee=1,
                minimum_initial_balance=50,
            ),
        ),
        AccountType(
            name=ACCOUNT_TYPES[1],
            account_rules=AccountRule(
                withdraw_fee=3,
                minimum_initial_balance=200,
            ),
        ),
    ],
)

santanderBank = Bank(
    name="Santander",
    account_types=[
        AccountType(
            name=ACCOUNT_TYPES[0],
            account_rules=AccountRule(
                withdraw_fee=1.5,
                minimum_initial_balance=65,
            ),
        ),
        AccountType(
            name=ACCOUNT_TYPES[1],
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
