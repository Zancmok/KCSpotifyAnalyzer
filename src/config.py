import os
import dotenv


dotenv.load_dotenv()


def _load_env(env_variable_name: str) -> str:
    if (return_value := os.getenv(env_variable_name)) is None:
        raise EnvironmentError(f".env file missing variable: '{env_variable_name}'")

    return return_value


# General
VERSION: str = _load_env("APP_VERSION")


# Flask
PORT: int = 5000
HOST: str = "0.0.0.0"
DEBUG: bool = True
FLASK_SECRET_KEY: str = _load_env("FLASK_SECRET_KEY")


# Spotify
SPOTIFY_REDIRECT_URI: str = "https://kcspotifyanalyzer.duckdns.org:9027/auth/callback"
SPOTIFY_CLIENT_ID: str = _load_env("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET: str = _load_env("SPOTIFY_CLIENT_SECRET")
