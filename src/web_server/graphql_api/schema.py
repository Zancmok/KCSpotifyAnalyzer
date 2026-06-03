import strawberry
from strawberry import Schema
from .resolvers.query_me import MeQuery


@strawberry.type
class Query(MeQuery):
    pass


schema: Schema = Schema(query=Query)
