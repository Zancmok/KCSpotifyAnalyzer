from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database_lib.models import User
from database_lib.repositories.UserRepository import UserRepository


def test_get_by_spotify_id_returns_user(session_factory: sessionmaker) -> None:
    """Verify the user is correctly retrieved by Spotify ID."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"
    name: str = "Hatsune Miku"

    with session_factory() as session, session.begin():
        session.add(
            User(
                spotify_id=spotify_id,
                name=name,
                image_url=None,
            )
        )

    # Act
    user: User | None = repository.get_by_spotify_id(spotify_id)

    # Assert
    assert user is not None
    assert user.spotify_id == spotify_id
    assert user.name == name


def test_get_by_spotify_id_returns_none(session_factory: sessionmaker) -> None:
    """Verify None is returned when the Spotify ID does not exist."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"

    # Act
    user: User | None = repository.get_by_spotify_id(spotify_id)

    # Assert
    assert user is None


def test_get_by_id_returns_user(session_factory: sessionmaker) -> None:
    """Verify the user is correctly retrieved by their ID."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    user_id: int = 39
    spotify_id: str = "spotify-39"
    name: str = "Hatsune Miku"

    with session_factory() as session, session.begin():
        session.add(
            User(
                id=user_id,
                spotify_id=spotify_id,
                name=name,
                image_url=None,
            )
        )

    # Act
    user: User | None = repository.get_by_id(user_id)

    # Assert
    assert user is not None
    assert user.id == user_id
    assert user.spotify_id == spotify_id
    assert user.name == name


def test_get_by_id_returns_none(session_factory: sessionmaker) -> None:
    """Verify None is returned when the User ID does not exist."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    user_id: int = 39

    # Act
    user: User | None = repository.get_by_id(user_id)

    # Assert
    assert user is None


def test_update_user_creates_user(session_factory: sessionmaker) -> None:
    """Verify a user is created upon there being no user with given spotify_id."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"
    name: str = "Hatsune Miku"
    image_url: str = "https://mikudajo.com/hatsune-miku.png"

    # Act
    user: User = repository.upsert_user(
        spotify_id=spotify_id,
        name=name,
        image_url=image_url
    )

    # Assert
    assert user.spotify_id == spotify_id
    assert user.name == name
    assert user.image_url == image_url


def test_update_user_updates_user_data(session_factory: sessionmaker) -> None:
    """Verify a user is updated upon existing priorly."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"
    old_name: str = "Hatsune Miku"
    new_name: str = "Kagamine Rin"

    with session_factory() as session, session.begin():
        session.add(
            User(
                spotify_id=spotify_id,
                name=old_name
            )
        )

    # Act
    user: User = repository.upsert_user(
        spotify_id=spotify_id,
        name=new_name
    )

    # Assert
    assert user.name == new_name


def test_get_last_upload_time_returns_upload_time(session_factory: sessionmaker) -> None:
    """Verify upload_time is returned when available."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"
    name: str = "Hatsune Miku"
    last_upload: datetime = datetime.now()

    with session_factory() as session, session.begin():
        session.add(
            User(
                spotify_id=spotify_id,
                name=name,
                last_upload=last_upload
            )
        )

    # Act
    received_datetime: datetime | None = repository.get_last_upload_time(spotify_id)

    # Assert
    assert received_datetime == last_upload


def test_get_last_upload_time_returns_none(session_factory: sessionmaker) -> None:
    """Verify None is returned when upload time isn't available."""
    # Arrange
    repository: UserRepository = UserRepository(session_factory)

    spotify_id: str = "spotify-39"

    # Act
    received_datetime: datetime | None = repository.get_last_upload_time(spotify_id)

    # Assert
    assert received_datetime is None
