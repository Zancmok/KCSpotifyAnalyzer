from typing import TYPE_CHECKING
from sqlalchemy import Enum as SQLEnum, CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .BaseModel import BaseModel
from ..enums.FriendshipStatus import FriendshipStatus


if TYPE_CHECKING:
    from .User import User


class Friendship(BaseModel):
    __tablename__ = "friendship"

    user1_id: Mapped[int] = mapped_column(primary_key=True)
    user2_id: Mapped[int] = mapped_column(primary_key=True)
    initiator_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    status: Mapped[FriendshipStatus] = mapped_column(
        SQLEnum(FriendshipStatus),
        nullable=False
    )

    __table_args__ = (
        CheckConstraint("user1_id < user2_id", name="ck_friendship_user_order"),
        UniqueConstraint("user1_id", "user2_id", name="uq_friendship_pair"),
        CheckConstraint("initiator_id = user1_id OR initiator_id = user2_id", name="ck_friendship_valid_initiator"),
    )

    user1: Mapped["User"] = relationship("User", foreign_keys=[user1_id], back_populates="friendships_as_user1")
    user2: Mapped["User"] = relationship("User", foreign_keys=[user2_id], back_populates="friendships_as_user2")
    initiator: Mapped["User"] = relationship("User", foreign_keys=[initiator_id], back_populates="initiated_friendships")
