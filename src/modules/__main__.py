from .uris import POSTGRES_URI
from .bank import Bank
from .user import User
from .accountRule import AccountRule
from .accountType import AccountType
from .account import Account
from .base import Base
import sqlalchemy.orm
from loguru import logger

postgres_engine = sqlalchemy.create_engine(url=POSTGRES_URI)

Base.metadata.create_all(bind=postgres_engine)

Session = sqlalchemy.orm.sessionmaker(bind=postgres_engine)
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
    name="Checking Account",
)

savingItau = AccountType(
    bank_id=itauBank.getId(),
    account_rule_id=savingItauRule.getId(),
    name="Saving Account",
)

checkingSantander = AccountType(
    bank_id=santanderBank.getId(),
    account_rule_id=checkingSantanderRule.getId(),
    name="Checking Account",
)

savingSantander = AccountType(
    bank_id=santanderBank.getId(),
    account_rule_id=savingSantanderRule.getId(),
    name="Saving Account",
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
