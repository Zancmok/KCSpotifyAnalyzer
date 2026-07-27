# pylint: disable=too-few-public-methods

from typing import Optional
import strawberry
from strawberry.types import Info
from database_lib.models import User as UserModel
from ..types import User


@strawberry.type
class MeQuery:
    """GraphQL query resolver for retrieving the current user.

    Provides fields related to the authenticated user from the request context.
    """
    @strawberry.field
    def me(self, info: Info) -> Optional[User]:
        """Retrieve the currently authenticated user.

        Returns the current user's GraphQL representation if a user is logged
        in, otherwise returns ``None``.
        """
        user_model: Optional[UserModel] = info.context["user"]

        if not user_model:
            return None

        return User(
            id=user_model.id,
            spotify_id=user_model.spotify_id,
            name=user_model.name,
            image_url=user_model.image_url
        )
