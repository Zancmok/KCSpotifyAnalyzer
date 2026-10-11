from sqlalchemy.orm import sessionmaker
from .. import _get_session_factory


class BaseRepository:
    """Base class for all repositories."""

    def __init__(self, session_factory: sessionmaker | None = None) -> None:
        """Initialize the repository.

        Args:
            session_factory: Optional session factory override.
        """
        self._session_factory: sessionmaker = (
            session_factory
            if session_factory is not None
            else _get_session_factory()
        )
