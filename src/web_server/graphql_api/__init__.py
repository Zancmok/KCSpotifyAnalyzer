from typing import Any, Optional, Sequence
from strawberry.flask.views import GraphQLView
from flask import session, Request, Response
from strawberry.http.ides import GraphQL_IDE
from strawberry.schema import BaseSchema
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL
import config
from database_lib.repositories.UserRepository import UserRepository


class MyGraphQLView(GraphQLView):
    """Custom GraphQL view with user-aware request context.

    Extends the default Strawberry GraphQL view to include authenticated user
    information in the GraphQL resolver context.
    """

    def __init__(self, schema: BaseSchema, graphql_ide: GraphQL_IDE | None = "graphiql",
                 allow_queries_via_get: bool = True, multipart_uploads_enabled: bool = False,
                 subscription_protocols: Sequence[str] = (
                         GRAPHQL_TRANSPORT_WS_PROTOCOL,
                         GRAPHQL_WS_PROTOCOL,
                 )):
        super().__init__(schema, graphql_ide, allow_queries_via_get, multipart_uploads_enabled, subscription_protocols)

        self.user_repository: UserRepository = UserRepository()

    def get_context(self, request: Request, response: Response) -> dict[str, Any]:
        """Create the GraphQL resolver context for a request.

        Adds the current request and the authenticated user, if available, to
        the context passed to GraphQL resolvers.
        """
        spotify_id: Optional[str] = session.get(config.SPOTIFY_ID_KEY)

        return {
            "request": request,
            "user": (
                self.user_repository.get_by_spotify_id(spotify_id)
                if spotify_id
                else None
            ),
        }
