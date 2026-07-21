import os
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
    except ValueError:
        raise EnvironmentError(f".env is not of type float: '{env_variable_name}'")


# General
DEBUG: bool = _load_bool("DEBUG")


# Spotify
SPOTIFY_CLIENT_ID: str = _load_str("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET: str = _load_str("SPOTIFY_CLIENT_SECRET")


# Database
MYSQL_PORT: int = int(_load_float("MYSQL_PORT"))
MYSQL_HOST: str = _load_str("MYSQL_HOST")
MYSQL_DATABASE: str = _load_str("MYSQL_DATABASE")
MYSQL_PASSWORD: str = _load_str("MYSQL_PASSWORD")
MYSQL_USER: str = _load_str("MYSQL_USER")
DATABASE_RECONNECTION_TIMEOUT: float = 1.0
