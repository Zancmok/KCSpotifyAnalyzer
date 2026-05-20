from flask import Blueprint, redirect, url_for, request
from flask.typing import ResponseReturnValue
from http import HTTPMethod
from spotipy import SpotifyOAuth, Spotify
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
        return redirect(url_for('pages.index'))

    auth_manager.get_access_token(code=code)

    print(spotify.current_user(), flush=True)

    return redirect(url_for('pages.home'))
