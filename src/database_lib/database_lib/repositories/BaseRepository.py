from sqlalchemy.orm import sessionmaker
from .. import _get_session_factory


class BaseRepository:
    """Base class for all repositories."""

    def __init__(self) -> None:
        """Initialize the repository."""
        self._session_factory: sessionmaker = _get_session_factory()
