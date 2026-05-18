import config
from flask import Flask
from routes import blueprints


def main() -> None:
    print(f"version: {config.VERSION}", flush=True)

    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=config.DEBUG
    )


if __name__ == "__main__":
    main()
