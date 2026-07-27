from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, DateTime, BigInteger, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .User import User
    from .Track import Track


class Listen(BaseModel):
    """Represents a single Spotify listening event.

    Each record captures one playback instance, including the user, track,
    playback duration, timestamp, platform, playback context, and other
    metadata reported by Spotify.
    """
    __tablename__ = "listen"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id")
    )
    track_id: Mapped[int] = mapped_column(
        ForeignKey("track.id")
    )
    ms_played: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    platform: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    country: Mapped[str] = mapped_column(
        String(8),
        nullable=False
    )
    ip_address: Mapped[str] = mapped_column(
        String(48),
        nullable=False
    )
    reason_start: Mapped[str] = mapped_column(
        String(16),
        nullable=False
    )
    reason_end: Mapped[str] = mapped_column(
        String(16),
        nullable=False
    )
    shuffle: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    skipped: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    offline: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    incognito: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], back_populates="listens")
    track: Mapped["Track"] = relationship("Track", foreign_keys=[track_id], back_populates="listens")
