# pylint: disable=too-few-public-methods

from typing import Optional
import strawberry


@strawberry.type
class User:
    """GraphQL representation of a user.

    Exposes user profile information returned through the GraphQL API.
    """
    id: int
    spotify_id: str
    name: str
    image_url: Optional[str]
