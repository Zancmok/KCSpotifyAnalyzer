import strawberry
from strawberry import Schema
from .types.User import User, get_user


@strawberry.type
class Query:
    users: list[User] = strawberry.field(resolver=get_user)


schema: Schema = Schema(query=Query)
