import os
import dotenv
from datetime import timedelta


dotenv.load_dotenv()


def _load_env(env_variable_name: str) -> str:
    if (return_value := os.getenv(env_variable_name)) is None:
        raise EnvironmentError(f".env file missing variable: '{env_variable_name}'")

    return return_value


# General
VERSION: str = _load_env("APP_VERSION")
DEBUG: bool = True


# Flask
PORT: int = 5000
HOST: str = "0.0.0.0"
FLASK_SECRET_KEY: str = _load_env("FLASK_SECRET_KEY")


# Spotify
SPOTIFY_REDIRECT_URI: str = "https://kcspotifyanalyzer.duckdns.org:9005/auth/callback"
SPOTIFY_CLIENT_ID: str = _load_env("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET: str = _load_env("SPOTIFY_CLIENT_SECRET")


# Database
MYSQL_PORT: int = 3306
MYSQL_HOST: str = "mysql"
MYSQL_DATABASE: str = "database"
MYSQL_ROOT_PASSWORD: str = "admin"
MYSQL_PASSWORD: str = "admin"
MYSQL_USER: str = "admin"
DATABASE_RECONNECTION_TIMEOUT: int | float = 1


# Session
SPOTIFY_ID_KEY: str = "spotify_id"
UPLOAD_TIME_LIMIT: timedelta = timedelta(minutes=5.0)
UPLOAD_FOLDER: str = "/uploads/"
