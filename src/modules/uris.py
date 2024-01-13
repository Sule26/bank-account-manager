from sqlalchemy.util import immutabledict
import os
import psycopg2
import MySQLdb
import sqlalchemy


POSTGRES_DRIVER = psycopg2.__name__.lower()
MYSQL_DRIVER = MySQLdb.__name__.lower()

POSTGRES_URI = sqlalchemy.URL(
    drivername=f"postgresql+{POSTGRES_DRIVER}",
    host=os.getenv("POSTGRES_HOST"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=5432,
    database=os.getenv("POSTGRES_DB"),
    query=immutabledict({"client_encoding": "utf8"}),
)


MYSQL_URI = sqlalchemy.URL(
    drivername=f"mysql+{MYSQL_DRIVER}",
    host=os.getenv('MYSQL_HOST'),
    username=os.getenv('MYSQL_USERNAME'),
    password=os.getenv('MYSQL_PASSWORD'),
    port=3306,
    database=os.getenv('MYSQL_DATABASE'),
    query=immutabledict({"charset": "utf8mb4"}),

)
