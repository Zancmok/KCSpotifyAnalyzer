# pylint: disable=too-few-public-methods

import strawberry
from strawberry import Schema
from .resolvers.query_me import MeQuery


@strawberry.type
class Query(MeQuery):
    """Root GraphQL query type.

    Provides the entry point for all read-only GraphQL operations exposed by
    the API.
    """


schema: Schema = Schema(query=Query)
