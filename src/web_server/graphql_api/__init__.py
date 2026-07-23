from typing import Any, Optional
from strawberry.flask.views import GraphQLView
from flask import session, Request, Response
import config
from database_lib.repositories.user_repository import get_by_spotify_id


class MyGraphQLView(GraphQLView):
    def get_context(self, request: Request, response: Response) -> dict[str, Any]:
        spotify_id: Optional[str] = session.get(config.SPOTIFY_ID_KEY)

        return {
            "request": request,
            "user": (
                get_by_spotify_id(spotify_id)
                if spotify_id
                else None
            ),
        }
