from http import HTTPMethod, HTTPStatus
from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from helpers import require_auth


blueprint: Blueprint = Blueprint(
    name="pages",
    import_name=__name__
)


@blueprint.route("/", methods=[HTTPMethod.GET])
def index() -> ResponseReturnValue:
    """Render the public landing page.

    Returns the index template for unauthenticated visitors.
    """
    return render_template("index.html"), HTTPStatus.OK


@blueprint.route("/home", methods=[HTTPMethod.GET])
@require_auth
def home() -> ResponseReturnValue:
    """Render the authenticated user's home page.

    Requires a valid authenticated session before rendering the home template.
    """
    return render_template("home.html"), HTTPStatus.OK
