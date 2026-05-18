import os
import dotenv

dotenv.load_dotenv()


# Environment Variables
if (FLASK_SECRET_KEY := os.getenv("FLASK_SECRET_KEY")) is None:
    raise Exception(".env misconfigured!")

if (VERSION := os.getenv("APP_VERSION")) is None:
    raise Exception("Dockerfile does not include a valid version!")


# Flask Config
PORT: int = 5000
HOST: str = "0.0.0.0"
DEBUG: bool = True
