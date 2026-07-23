from typing import Optional
import strawberry


@strawberry.type
class User:
    """ A GraphQL User type. """
    
    id: int
    spotify_id: str
    name: str
    image_url: Optional[str]
