from typing import TYPE_CHECKING, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .Friendship import Friendship


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    spotify_id: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        unique=True
    )
    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    image_url: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True
    )

    friendships_as_user1: Mapped[list["Friendship"]] = relationship(
        "Friendship",
        foreign_keys="Friendship.user1_id",
        back_populates="user1",
    )

    friendships_as_user2: Mapped[list["Friendship"]] = relationship(
        "Friendship",
        foreign_keys="Friendship.user2_id",
        back_populates="user2",
    )

    initiated_friendships: Mapped[list["Friendship"]] = relationship(
        "Friendship",
        foreign_keys="Friendship.initiator_id",
        back_populates="initiator",
    )
