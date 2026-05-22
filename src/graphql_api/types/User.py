from typing import Optional
import strawberry
from database.models import User as DBUser
import database.repositories.user_repository as user_repository


@strawberry.type
class User:
    id: int
    spotify_id: str
    name: str
    image_url: Optional[str]


def get_user(spotify_id: str) -> list[User]:
    user: Optional[DBUser] = user_repository.get_by_spotify_id(spotify_id)

    if not user:
        return []

    return [User(
        id=user.id,
        spotify_id=user.spotify_id,
        name=user.name,
        image_url=user.image_url
    )]
