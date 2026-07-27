from typing import Any, Optional
from strawberry.flask.views import GraphQLView
from flask import session, Request, Response
import config
from database_lib.repositories.user_repository import get_by_spotify_id


class MyGraphQLView(GraphQLView):
    """Custom GraphQL view with user-aware request context.

    Extends the default Strawberry GraphQL view to include authenticated user
    information in the GraphQL resolver context.
    """
    def get_context(self, request: Request, response: Response) -> dict[str, Any]:
        """Create the GraphQL resolver context for a request.

        Adds the current request and the authenticated user, if available, to
        the context passed to GraphQL resolvers.
        """
        spotify_id: Optional[str] = session.get(config.SPOTIFY_ID_KEY)

        return {
            "request": request,
            "user": (
                get_by_spotify_id(spotify_id)
                if spotify_id
                else None
            ),
        }
