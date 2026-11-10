from http import HTTPStatus, HTTPMethod
from datetime import datetime, timezone
from flask import jsonify
from flask.typing import ResponseReturnValue
import config
from .base_route import BaseRoute


class CommonRoute(BaseRoute):
    def __init__(self, name: str, import_name: str) -> None:
        super().__init__(name, import_name)

        # Routes
        self.blueprint.add_url_rule("/ping", methods=[HTTPMethod.GET])
        self.blueprint.add_url_rule("/health", methods=[HTTPMethod.GET])

    @staticmethod
    def ping() -> ResponseReturnValue:
        """Return a basic service availability response.

        Used to verify that the application is running and responding to requests.
        """
        return jsonify({
            "status": "ok"
        }), HTTPStatus.OK

    @staticmethod
    def health() -> ResponseReturnValue:
        """Return detailed application health information.

        Includes the service status, current UTC timestamp, and application
        version.
        """
        return jsonify({
            "status": "ok",
            "service": "kc-spotify-analyzer",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "app_version": config.VERSION
        }), HTTPStatus.OK
