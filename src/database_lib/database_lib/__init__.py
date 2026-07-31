from time import sleep
from typing import Any
from sqlalchemy.exc import OperationalError
import sqlalchemy
from sqlalchemy import Engine, text, URL, CursorResult
from sqlalchemy.orm import sessionmaker
from .models.BaseModel import BaseModel

_SQL_ENGINE: Engine | None = None
_SESSION_FACTORY: sessionmaker | None = None


def initialize(username: str, password: str, host: str, port: int, database: str,
               reconnection_timeout: float | int = 1.0, debug: bool = False) -> None:
    """
    Initialize the SQLAlchemy database engine.

    Creates a MySQL SQLAlchemy engine using the provided connection details,
    waits until a successful database connection can be established, and then
    creates all tables defined in the SQLAlchemy metadata.

    Args:
        username: Database username.
        password: Database password.
        host: Database server hostname or IP address.
        port: Database server port.
        database: Name of the database to connect to.
        reconnection_timeout: Time in seconds to wait before retrying after a
            failed connection attempt.
        debug: Whether to enable SQLAlchemy engine debug logging.

    Raises:
        OperationalError: Not raised directly; connection errors are retried
            until a connection succeeds.
    """
    global _SQL_ENGINE, _SESSION_FACTORY  # pylint: disable=global-statement
    _SQL_ENGINE = sqlalchemy.create_engine(URL.create(
        drivername="mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    ), echo=debug)

    while True:
        try:
            with _SQL_ENGINE.connect() as conn:
                result: CursorResult[Any] = conn.execute(text("SELECT 'Miku Dayo'"))
                print(result.fetchone(), flush=True)

            break
        except OperationalError:
            print(f"Retrying connection in {reconnection_timeout}s...", flush=True)
            sleep(reconnection_timeout)

    BaseModel.metadata.create_all(_SQL_ENGINE)

    _SESSION_FACTORY = sessionmaker(
        bind=_SQL_ENGINE,
        expire_on_commit=False
    )


def _get_sql_engine() -> Engine:
    """
    Retrieve the initialized SQLAlchemy engine.

    Returns:
        The active SQLAlchemy engine instance.

    Raises:
        Exception: If the database has not been initialized yet.
    """
    if _SQL_ENGINE is None:
        raise RuntimeError("Not initialized!")

    return _SQL_ENGINE


def _get_session_factory() -> sessionmaker:
    """Retrieve the initialized SQLAlchemy session factory.

    Returns:
        The configured session factory used to create database sessions.

    Raises:
        RuntimeError: If the database has not been initialized.
    """
    if _SESSION_FACTORY is None:
        raise RuntimeError("Not initialized!")

    return _SESSION_FACTORY


__all__ = [
    "initialize",
]
