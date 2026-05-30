from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from http import HTTPMethod, HTTPStatus
from helpers import require_auth


blueprint: Blueprint = Blueprint(
    name="pages",
    import_name=__name__
)


@blueprint.route("/", methods=[HTTPMethod.GET])
def index() -> ResponseReturnValue:
    return render_template("index.html"), HTTPStatus.OK


@blueprint.route("/home", methods=[HTTPMethod.GET])
@require_auth
def home() -> ResponseReturnValue:
    return render_template("home.html"), HTTPStatus.OK
