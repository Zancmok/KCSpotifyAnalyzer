from typing import Optional
import strawberry
from database_lib.models import User as DBUser
import database_lib.repositories.user_repository as user_repository


@strawberry.type
class User:
    id: int
    spotify_id: str
    name: str
    image_url: Optional[str]


def get_user(id: int) -> list[User]:
    user: Optional[DBUser] = user_repository.get_by_id(id)

    if not user:
        return []

    return [User(
        id=user.id,
        spotify_id=user.spotify_id,
        name=user.name,
        image_url=user.image_url
    )]
