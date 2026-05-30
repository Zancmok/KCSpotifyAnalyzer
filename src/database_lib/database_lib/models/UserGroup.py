from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel


if TYPE_CHECKING:
    from .User import User
    from .Group import Group


class UserGroup(BaseModel):
    __tablename__ = "usergroup"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        primary_key=True
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey("group.id"),
        primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], back_populates="user_groups")
    group: Mapped["Group"] = relationship("Group", foreign_keys=[group_id], back_populates="user_groups")
