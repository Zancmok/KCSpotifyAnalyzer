from http import HTTPStatus, HTTPMethod
from datetime import datetime, timezone
from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue
import config


blueprint: Blueprint = Blueprint(
    name="common",
    import_name=__name__
)


@blueprint.route("/ping", methods=[HTTPMethod.GET])
def ping() -> ResponseReturnValue:
    return jsonify({
        "status": "ok"
    }), HTTPStatus.OK


@blueprint.route("/health", methods=[HTTPMethod.GET])
def health() -> ResponseReturnValue:
    return jsonify({
        "status": "ok",
        "service": "kc-spotify-analyzer",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app_version": config.VERSION
    }), HTTPStatus.OK
