from typing import Optional
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import User
from .. import get_sql_engine


def get_by_spotify_id(spotify_id: str) -> Optional[User]:
    """Retrieve a user by their Spotify ID.

    Returns the matching user if one exists, otherwise ``None``.
    """
    with Session(get_sql_engine()) as session:
        return session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()


def get_by_id(user_id: int) -> Optional[User]:
    """Retrieve a user by their database ID.

    Returns the matching user if one exists, otherwise ``None``.
    """
    with Session(get_sql_engine()) as session:
        return session.execute(select(User).where(User.id == user_id)).scalars().first()


def update_user(spotify_id: str, name: str, image_url: Optional[str]) -> User:
    """Create or update a user.

    If a user with the given Spotify ID does not exist, a new user is created.
    Otherwise, the user's profile information is updated. The persisted user is
    returned.
    """
    with Session(get_sql_engine()) as session:
        user: Optional[User] = session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

        if not user:
            user: User = User(
                spotify_id=spotify_id,
                name=name,
                image_url=image_url
            )

            session.add(user)
        else:
            user.name = name
            user.image_url = image_url

        session.commit()

        session.refresh(user)

        return user


def get_last_upload_time(spotify_id: str) -> Optional[datetime]:
    """Retrieve the timestamp of a user's most recent data upload.

    Returns ``None`` if the user does not exist or has never uploaded data.
    """
    with Session(get_sql_engine()) as session:
        user: Optional[User] = session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

        if not user:
            return None

        return user.last_upload


def update_upload_time(spotify_id: str) -> None:
    """Update a user's last upload timestamp to the current time.

    Does nothing if no user with the given Spotify ID exists.
    """
    with Session(get_sql_engine()) as session:
        user: Optional[User] = session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

        if not user:
            return

        user.last_upload = datetime.now()

        session.commit()
