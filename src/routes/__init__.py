from flask import Blueprint
from .common import blueprint as common_blueprint
from .pages import blueprint as pages_blueprint
from .auth import blueprint as auth_blueprint


blueprints: list[Blueprint] = [
    common_blueprint,
    pages_blueprint,
    auth_blueprint
]


__all__ = [
    "blueprints"
]
