from .uris import POSTGRES_URI, MYSQL_URI
from .bank import Bank
from .user import User
from .accountRule import AccountRule
from .accountType import AccountType
from .account import Account
from .base import Base
import sqlalchemy.orm
from loguru import logger

ACCOUNT_TYPES = ["Checking Account", "Saving Account"]

engine = sqlalchemy.create_engine(url=POSTGRES_URI)

#TODO: Solve the issues related to MySQL Syntax
# engine = sqlalchemy.create_engine(url=MYSQL_URI)


Base.metadata.create_all(bind=engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# Creating Banks
itauBank = Bank(name="Itaú")
santanderBank = Bank(name="Bradesco")

# Adding Banks to the database
session.add_all(
    [
        itauBank,
        santanderBank,
    ]
)
session.commit()

# Getting Banks uuid from the database
itauBank = session.get(entity=Bank, ident=itauBank.getId())
santanderBank = session.get(entity=Bank, ident=santanderBank.getId())

# Creating Account Rules
checkingItauRule = AccountRule(
    withdraw_fee=1,
    minimum_initial_balance=50,
)

savingItauRule = AccountRule(
    withdraw_fee=3,
    minimum_initial_balance=200,
)

checkingSantanderRule = AccountRule(
    withdraw_fee=1.5,
    minimum_initial_balance=65,
)

savingSantanderRule = AccountRule(
    withdraw_fee=3.75,
    minimum_initial_balance=175,
)

# Adding Account Rules to the database
session.add_all(
    [
        checkingItauRule,
        savingItauRule,
        checkingSantanderRule,
        savingSantanderRule,
    ]
)
session.commit()

# Getting AccountRule uuid from the database
checkingItauRule = session.get(
    entity=AccountRule,
    ident=checkingItauRule.getId(),
)
savingItauRule = session.get(
    entity=AccountRule,
    ident=savingItauRule.getId(),
)
checkingSantanderRule = session.get(
    entity=AccountRule,
    ident=checkingSantanderRule.getId(),
)
savingSantanderRule = session.get(
    entity=AccountRule,
    ident=checkingSantanderRule.getId(),
)

# Creating Account Types
checkingItau = AccountType(
    bank_id=itauBank.getId(),
    account_rule_id=checkingItauRule.getId(),
    name=ACCOUNT_TYPES[0],
)

savingItau = AccountType(
    bank_id=itauBank.getId(),
    account_rule_id=savingItauRule.getId(),
    name=ACCOUNT_TYPES[1],
)

checkingSantander = AccountType(
    bank_id=santanderBank.getId(),
    account_rule_id=checkingSantanderRule.getId(),
    name=ACCOUNT_TYPES[0],
)

savingSantander = AccountType(
    bank_id=santanderBank.getId(),
    account_rule_id=savingSantanderRule.getId(),
    name=ACCOUNT_TYPES[1],
)

# Adding Account Types to the database

session.add_all(
    [
        checkingItau,
        savingItau,
        checkingSantander,
        savingSantander,
    ]
)
session.commit()

# Getting AccountType uuid from the database
checkingItau = session.get(
    entity=AccountType,
    ident=checkingItau.getId(),
)

savingItau = session.get(
    entity=AccountType,
    ident=savingItau.getId(),
)

checkingSantander = session.get(
    entity=AccountType,
    ident=checkingSantander.getId(),
)

savingSantander = session.get(
    entity=AccountType,
    ident=savingSantander.getId(),
)
