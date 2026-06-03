from typing import Optional
import strawberry


@strawberry.type
class User:
    id: int
    spotify_id: str
    name: str
    image_url: Optional[str]
