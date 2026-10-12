from datetime import datetime
from database_lib.models import User
from database_lib.repositories.UserRepository import UserRepository


def test_get_by_spotify_id_returns_user(
        user_repository: UserRepository,
        user: User
) -> None:
    """Verify the user is correctly retrieved by Spotify ID."""

    # Act
    received_user: User | None = user_repository.get_by_spotify_id(user.spotify_id)

    # Assert
    assert received_user is not None
    assert received_user.spotify_id == user.spotify_id
    assert received_user.name == user.name


def test_get_by_spotify_id_returns_none(
        user_repository: UserRepository
) -> None:
    """Verify None is returned when the Spotify ID does not exist."""
    # Arrange
    spotify_id: str = "spotify-39"

    # Act
    user: User | None = user_repository.get_by_spotify_id(spotify_id)

    # Assert
    assert user is None


def test_get_by_id_returns_user(
        user_repository: UserRepository,
        user: User
) -> None:
    """Verify the user is correctly retrieved by their ID."""
    # Act
    received_user: User | None = user_repository.get_by_id(user.id)

    # Assert
    assert received_user is not None
    assert received_user.id == user.id
    assert received_user.spotify_id == user.spotify_id
    assert received_user.name == user.name


def test_get_by_id_returns_none(
        user_repository: UserRepository
) -> None:
    """Verify None is returned when the User ID does not exist."""
    # Arrange
    user_id: int = 39

    # Act
    user: User | None = user_repository.get_by_id(user_id)

    # Assert
    assert user is None


def test_upsert_user_creates_user(
        user_repository: UserRepository
) -> None:
    """Verify a user is created upon there being no user with given spotify_id."""
    # Arrange
    spotify_id: str = "spotify-39"
    name: str = "Hatsune Miku"
    image_url: str = "https://mikudajo.com/hatsune-miku.png"

    # Act
    user: User = user_repository.upsert_user(
        spotify_id=spotify_id,
        name=name,
        image_url=image_url
    )

    # Assert
    assert user.spotify_id == spotify_id
    assert user.name == name
    assert user.image_url == image_url


def test_upsert_user_updates_user_data(
        user_repository: UserRepository,
        user: User
) -> None:
    """Verify a user is updated upon existing priorly."""
    # Arrange
    new_name: str = f"New {user.name}"

    # Act
    user: User = user_repository.upsert_user(
        spotify_id=user.spotify_id,
        name=new_name,
        image_url=user.image_url
    )

    # Assert
    assert user.name == new_name


def test_get_last_upload_time_returns_upload_time(
        user_repository: UserRepository,
        user2: User
) -> None:
    """Verify upload_time is returned when available."""
    # Act
    received_datetime: datetime | None = user_repository.get_last_upload_time(user2.spotify_id)

    # Assert
    assert received_datetime == user2.last_upload


def test_get_last_upload_time_returns_none(
        user_repository: UserRepository,
        user: User
) -> None:
    """Verify None is returned when upload time isn't available."""
    # Act
    received_datetime: datetime | None = user_repository.get_last_upload_time(user.spotify_id)

    # Assert
    assert received_datetime is None
