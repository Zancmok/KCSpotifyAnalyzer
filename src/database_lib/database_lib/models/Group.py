from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .User import User
    from .UserGroup import UserGroup


class Group(BaseModel):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    image_url: Mapped[Optional[str]] = mapped_column(
        String(256),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    owner: Mapped["User"] = relationship("User", foreign_keys=[owner_id], back_populates="owned_groups")

    user_groups: Mapped[list["UserGroup"]] = relationship(
        "UserGroup",
        foreign_keys="UserGroup.group_id",
        back_populates="group",
    )
    