from typing import Optional
import strawberry
from strawberry.types import Info
from database_lib.models import User as UserModel
from ..types import User


@strawberry.type
class MeQuery:
    """ A GraphQL Query denoting self. """
    
    @strawberry.field
    def me(self, info: Info) -> Optional[User]:
        """ Returns info about self. """
        
        user_model: Optional[UserModel] = info.context["user"]

        if not user_model:
            return None

        return User(
            id=user_model.id,
            spotify_id=user_model.spotify_id,
            name=user_model.name,
            image_url=user_model.image_url
        )
