import os
import psycopg2
import sqlalchemy

POSTGRES_DRIVER = psycopg2.__name__.lower()

POSTGRES_URI = sqlalchemy.URL(
    drivername=f"postgresql+{POSTGRES_DRIVER}",
    host=os.getenv("POSTGRES_HOST"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=5432,
    database=os.getenv("POSTGRES_DB"),
    query={"client_encoding": "utf8"},
)
