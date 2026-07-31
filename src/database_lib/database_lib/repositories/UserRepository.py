from datetime import datetime, timezone
from sqlalchemy import select
from .BaseRepository import BaseRepository
from ..models import User


class UserRepository(BaseRepository):
    """Repository for managing User database operations."""

    def get_by_spotify_id(self, spotify_id: str) -> User | None:
        """Retrieve a user by their Spotify ID.

        Args:
            spotify_id: The Spotify user identifier to search for.

        Returns:
            The matching User instance if found, otherwise ``None``.
        """
        with self._session_factory() as session:
            return session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

    def get_by_id(self, user_id: int) -> User | None:
        """Retrieve a user by their database ID.

        Args:
            user_id: The database ID to search for.

        Returns:
             The matching user if one exists, otherwise ``None``.
        """
        with self._session_factory() as session:
            return session.execute(select(User).where(User.id == user_id)).scalars().first()

    def update_user(self, spotify_id: str, name: str, image_url: str | None) -> User:
        """
        Create or update a user.

        If a user with the given Spotify ID does not exist, a new user is created.
        Otherwise, the user's profile information is updated. The persisted user is
        returned after the transaction is committed.

        Args:
            spotify_id (str): The Spotify identifier of the user.
            name (str): The user's display name.
            image_url (str | None): The URL of the user's profile image, if available.

        Returns:
            User: The created or updated persisted user.
        """
        with self._session_factory() as session, session.begin():
            user: User | None = session.execute(
                select(User).where(User.spotify_id == spotify_id)).scalars().first()

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

            return user

    def get_last_upload_time(self, spotify_id: str) -> datetime | None:
        """
        Retrieve the timestamp of a user's most recent data upload.

        Returns None if the user does not exist or has never uploaded any data.

        Args:
            spotify_id (str): The Spotify identifier of the user.

        Returns:
            datetime | None: The timestamp of the user's most recent upload,
            or None if no upload exists.
        """
        with self._session_factory() as session:
            user: User | None = session.execute(
                select(User).where(User.spotify_id == spotify_id)).scalars().first()

            if not user:
                return None

            return user.last_upload

    def update_upload_time(self, spotify_id: str) -> None:
        """
        Update a user's last upload timestamp to the current time.

        Does nothing if no user with the given Spotify ID exists.

        Args:
            spotify_id (str): The Spotify identifier of the user.
        """
        with self._session_factory() as session, session.begin():
            user: User | None = session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

            if not user:
                return

            user.last_upload = datetime.now(timezone.utc)
