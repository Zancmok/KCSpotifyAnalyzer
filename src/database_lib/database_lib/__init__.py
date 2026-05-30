from time import sleep
from typing import Any, Optional
from sqlalchemy.exc import OperationalError
import sqlalchemy
from sqlalchemy import Engine, text, URL, CursorResult
from .models.BaseModel import BaseModel

_sql_engine: Optional[Engine] = None


def initialize(username: str, password: str, host: str, port: int, database: str,
               reconnection_timeout: float | int = 1.0, debug: bool = False) -> None:
    global _sql_engine
    _sql_engine = sqlalchemy.create_engine(URL.create(
        drivername="mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    ), echo=debug)

    while True:
        try:
            with _sql_engine.connect() as conn:
                result: CursorResult[Any] = conn.execute(text("SELECT 'Miku Dayo'"))
                print(result.fetchone(), flush=True)

            break
        except OperationalError:
            print(f"Retrying connection in {reconnection_timeout}s...", flush=True)
            sleep(reconnection_timeout)

    BaseModel.metadata.create_all(_sql_engine)


def get_sql_engine() -> Engine:
    if not _sql_engine:
        raise Exception("Not initialized!")

    return _sql_engine


__all__ = [
    "initialize",
    "get_sql_engine"
]
