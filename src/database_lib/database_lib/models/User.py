from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .Friendship import Friendship
    from .Group import Group
    from .UserGroup import UserGroup


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
    joined_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    last_upload: Mapped[datetime] = mapped_column(
        DateTime,
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

    owned_groups: Mapped[list["Group"]] = relationship(
        "Group",
        foreign_keys="Group.owner_id",
        back_populates="owner",
    )

    user_groups: Mapped[list["UserGroup"]] = relationship(
        "UserGroup",
        foreign_keys="UserGroup.user_id",
        back_populates="user",
    )
