import config
from flask import Flask
from strawberry.flask.views import GraphQLView
from routes import blueprints
import database.database as database
from graphql_api.schema import schema


def main() -> None:
    print(f"version: {config.VERSION}", flush=True)

    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql_view", schema=schema)
    )

    database.initialize()

    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=config.DEBUG
    )


if __name__ == "__main__":
    main()
