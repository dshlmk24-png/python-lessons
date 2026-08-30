import os

from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Не задана переменная DATABASE_URL")

engine = create_engine(DATABASE_URL)


def execute_query(query, params=None):
    with engine.begin() as connection:
        result = connection.execute(
            text(query),
            params or {}
        )
        return result
