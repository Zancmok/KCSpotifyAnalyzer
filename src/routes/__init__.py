from flask import Blueprint
from .common import blueprint as common_blueprint
from .pages import blueprint as pages_blueprint
from .auth import blueprint as auth_blueprint
from .user_data import blueprint as user_data_blueprint


blueprints: list[Blueprint] = [
    common_blueprint,
    pages_blueprint,
    auth_blueprint,
    user_data_blueprint
]


__all__ = [
    "blueprints"
]
