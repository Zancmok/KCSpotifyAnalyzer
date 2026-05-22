import functools
from typing import Callable, Any
from flask import session, redirect, url_for
import config


def require_auth(function: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        if not session.get(config.SPOTIFY_ID_KEY):
            return redirect(url_for("auth.login"))
        return function(*args, **kwargs)

    return wrapper
