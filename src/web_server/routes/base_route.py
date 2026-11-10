from flask import Blueprint


class BaseRoute:
    def __init__(self, name: str, import_name: str) -> None:
        self.blueprint: Blueprint = Blueprint(name, import_name)
