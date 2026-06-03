import config
from flask import Flask
from strawberry.flask.views import GraphQLView
from routes import blueprints
from database_lib import initialize as initialize_database
from graphql_api import MyGraphQLView
from graphql_api.schema import schema


def main() -> None:
    print(f"version: {config.VERSION}", flush=True)

    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.add_url_rule(
        "/graphql",
        view_func=MyGraphQLView.as_view(
            "graphql_view",
            schema=schema,
        )
    )

    initialize_database(
        username=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        database=config.MYSQL_DATABASE,
        reconnection_timeout=config.DATABASE_RECONNECTION_TIMEOUT,
        debug=config.DEBUG
    )

    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=config.DEBUG
    )


if __name__ == "__main__":
    main()
