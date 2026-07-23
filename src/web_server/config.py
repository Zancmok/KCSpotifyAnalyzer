import os
from datetime import timedelta
import dotenv


dotenv.load_dotenv()


def _load_env(env_variable_name: str) -> str:
    if (return_value := os.getenv(env_variable_name)) is None:
        raise EnvironmentError(f".env file missing variable: '{env_variable_name}'")

    return return_value


def _load_str(env_variable_name: str) -> str:
    return _load_env(env_variable_name)


def _load_bool(env_variable_name: str) -> bool:
    return _load_env(env_variable_name).lower() == "true"


def _load_float(env_variable_name: str) -> float:
    try:
        return float(_load_env(env_variable_name))
    except ValueError as exc:
        raise EnvironmentError(f".env is not of type float: '{env_variable_name}'") from exc


# General
VERSION: str = _load_str("APP_VERSION")
DEBUG: bool = _load_bool("DEBUG")

# Flask
PORT: int = int(_load_float("INTERNAL_PORT"))
HOST: str = _load_str("INTERNAL_HOST")
FLASK_SECRET_KEY: str = _load_str("FLASK_SECRET_KEY")

# Spotify
SPOTIFY_REDIRECT_URI: str = _load_str("SPOTIFY_REDIRECT_URI")
SPOTIFY_CLIENT_ID: str = _load_str("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET: str = _load_str("SPOTIFY_CLIENT_SECRET")

# Database
MYSQL_PORT: int = int(_load_float("MYSQL_PORT"))
MYSQL_HOST: str = _load_str("MYSQL_HOST")
MYSQL_DATABASE: str = _load_str("MYSQL_DATABASE")
MYSQL_PASSWORD: str = _load_str("MYSQL_PASSWORD")
MYSQL_USER: str = _load_str("MYSQL_USER")
DATABASE_RECONNECTION_TIMEOUT: float = 1.0

# Session
SPOTIFY_ID_KEY: str = "spotify_id"
UPLOAD_TIME_LIMIT: timedelta = timedelta(minutes=5.0)
UPLOAD_FOLDER: str = _load_str("UPLOAD_FOLDER")
