# pylint: disable=redefined-outer-name
from datetime import datetime

import pytest
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database_lib.models.BaseModel import BaseModel
from database_lib.models import User
from database_lib.repositories.UserRepository import UserRepository


@pytest.fixture
def session_factory() -> sessionmaker:
    """Create a temporary in-memory SQLite session factory.

    Returns:
        sessionmaker: A SQLAlchemy session factory connected to
            an in-memory SQLite database.
    """
    engine: Engine = create_engine(
        "sqlite://",
        connect_args={
            "check_same_thread": False
        },
        poolclass=StaticPool,
    )

    BaseModel.metadata.create_all(engine)

    return sessionmaker(
        bind=engine,
        expire_on_commit=False
    )


@pytest.fixture
def user_repository(session_factory: sessionmaker) -> UserRepository:
    """Returns a new UserRepository."""
    return UserRepository(session_factory)


@pytest.fixture
def user(session_factory: sessionmaker) -> User:
    """Returns a new User with only the necessities."""
    user: User = User(
        spotify_id="spotify-01",
        name="Hatsune Miku"
    )

    with session_factory.begin() as session:
        session.add(user)

    return user


@pytest.fixture
def user2(session_factory: sessionmaker) -> User:
    """Returns a new User with all properties."""
    user: User = User(
        spotify_id="spotify-02",
        name="Kagamine Rin",
        image_url="https://len.com/len.png",
        last_upload=datetime.now(),
    )

    with session_factory.begin() as session:
        session.add(user)

    return user
