from http import HTTPMethod, HTTPStatus
from flask import render_template
from flask.typing import ResponseReturnValue
from helpers import require_auth
from .base_route import BaseRoute


class PagesRoute(BaseRoute):
    def __init__(self, name: str, import_name: str) -> None:
        super().__init__(name, import_name)

        # Routes
        self.blueprint.add_url_rule(
            "/",
            methods=[HTTPMethod.GET],
            view_func=self.index
        )
        self.blueprint.add_url_rule(
            "/health",
            methods=[HTTPMethod.GET],
            view_func=self.home
        )


    @staticmethod
    def index() -> ResponseReturnValue:
        """Render the public landing page.

        Returns the index template for unauthenticated visitors.
        """
        return render_template("index.html"), HTTPStatus.OK


    @staticmethod
    @require_auth
    def home() -> ResponseReturnValue:
        """Render the authenticated user's home page.

        Requires a valid authenticated session before rendering the home template.
        """
        return render_template("home.html"), HTTPStatus.OK
