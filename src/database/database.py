from time import sleep
from typing import Any
from sqlalchemy.exc import OperationalError
import config
import sqlalchemy
from sqlalchemy import Engine, text, URL, CursorResult
from .models.BaseModel import BaseModel

sql_engine: Engine = sqlalchemy.create_engine(URL.create(
    drivername="mysql+pymysql",
    username=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD,
    host=config.MYSQL_HOST,
    port=config.MYSQL_PORT,
    database=config.MYSQL_DATABASE,
), echo=config.DEBUG)


def initialize() -> None:
    while True:
        try:
            with sql_engine.connect() as conn:
                result: CursorResult[Any] = conn.execute(text("SELECT 'Miku Dayo'"))
                print(result.fetchone(), flush=True)

            break
        except OperationalError:
            print(f"Retrying connection in {config.DATABASE_RECONNECTION_TIMEOUT}s...", flush=True)
            sleep(config.DATABASE_RECONNECTION_TIMEOUT)

    BaseModel.metadata.create_all(sql_engine)
