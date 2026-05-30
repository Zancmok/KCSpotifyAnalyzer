from typing import Any, Optional
from flask import Blueprint, redirect, url_for, request, session
from flask.typing import ResponseReturnValue
from http import HTTPMethod, HTTPStatus
from spotipy import SpotifyOAuth, Spotify
from database_lib.models import User
import database_lib.repositories.user_repository as user_repository
from helpers import require_auth
import config

blueprint: Blueprint = Blueprint(
    name="auth",
    import_name=__name__,
    url_prefix="/auth"
)
auth_manager: SpotifyOAuth = SpotifyOAuth(
    client_id=config.SPOTIFY_CLIENT_ID,
    client_secret=config.SPOTIFY_CLIENT_SECRET,
    redirect_uri=config.SPOTIFY_REDIRECT_URI
)
spotify: Spotify = Spotify(auth_manager=auth_manager)


@blueprint.route("/login", methods=[HTTPMethod.GET])
def login() -> ResponseReturnValue:
    return redirect(auth_manager.get_authorize_url())


@blueprint.route("/callback", methods=[HTTPMethod.GET])
def callback() -> ResponseReturnValue:
    if (code := request.args.to_dict().get('code')) is None:
        print(f"Code missing!", flush=True)
        return redirect(url_for('auth.login'))

    auth_manager.get_access_token(code=code)

    spotify_user_data: dict[str, Any] = spotify.current_user()

    if not (spotify_id := spotify_user_data.get("id")) or not isinstance(spotify_id, str):
        print(f"Spotify id inside of: '{spotify_user_data}' is invalid!", flush=True)
        return redirect(url_for('pages.index'))

    if not (name := spotify_user_data.get("display_name")) or not isinstance(name, str):
        print(f"Spotify name inside of: '{spotify_user_data}' is invalid!", flush=True)
        return redirect(url_for('pages.index'))

    if not (images := spotify_user_data.get("images")) or not isinstance(images, list):
        print(f"Spotify images inside of: '{spotify_user_data}' is invalid!", flush=True)
        return redirect(url_for('pages.index'))

    image_url: Optional[str] = None
    curr_width: int = -1
    for image in images:
        if not isinstance(image, dict):
            continue

        if not (width := image.get("width")) or not isinstance(width, int):
            continue

        if width > curr_width:
            curr_width = width
            image_url = image.get("url")

    user_repository.update_user(
        spotify_id=spotify_id,
        name=name,
        image_url=image_url
    )

    session[config.SPOTIFY_ID_KEY] = spotify_id

    return redirect(url_for('pages.home'))
