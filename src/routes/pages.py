from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from HTTPCode import HTTPCode
from HTTPMethod import HTTPMethod


blueprint: Blueprint = Blueprint(
    name="pages",
    import_name=__name__
)


@blueprint.route("/", methods=[HTTPMethod.GET])
def index() -> ResponseReturnValue:
    return render_template("index.html"), HTTPCode.OK
