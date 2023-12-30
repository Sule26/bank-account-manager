from .uris import POSTGRES_URI
from .bank import Bank
from .user import User
from .accountRule import AccountRule
from .accountType import AccountType
from .account import Account
from .base import Base
import psycopg2
import sqlalchemy.orm

postgres_engine = sqlalchemy.create_engine(url=POSTGRES_URI)

Base.metadata.create_all(bind=postgres_engine)

# Session = sqlalchemy.orm.sessionmaker(bind=postgres_engine)

# session = Session()

# session.commit()
