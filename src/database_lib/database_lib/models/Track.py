from typing import TYPE_CHECKING
from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .Listen import Listen


class Track(BaseModel):
    """Represents a Spotify track.

    Stores the Spotify identifier for a track and provides access to all
    listening events associated with it.
    """
    __tablename__ = "track"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    spotify_id: Mapped[str] = mapped_column(
        String(32),
        nullable=False
    )

    listens: Mapped[list["Listen"]] = relationship(
        "Listen",
        foreign_keys="Listen.track_id",
        back_populates="track"
    )
