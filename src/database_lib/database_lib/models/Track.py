from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import String, DateTime, func, BigInteger, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .Listen import Listen


class Track(BaseModel):
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
