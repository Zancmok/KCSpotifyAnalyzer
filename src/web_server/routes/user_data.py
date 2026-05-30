import zipfile
from typing import Any, Optional
from flask import Blueprint, session, request
from flask.typing import ResponseReturnValue
from http import HTTPMethod, HTTPStatus
from werkzeug.datastructures import FileStorage
from database_lib.models import User
import database_lib.repositories.user_repository as user_repository
from helpers import require_auth
import config

blueprint: Blueprint = Blueprint(
    name="user_data",
    import_name=__name__,
    url_prefix="/user_data"
)


@blueprint.route("/me", methods=[HTTPMethod.POST])
@require_auth
def me() -> ResponseReturnValue:
    user: Optional[User] = user_repository.get_by_spotify_id(session.get(config.SPOTIFY_ID_KEY, ''))
    if not user:
        return {}, HTTPStatus.BAD_REQUEST

    return {
        "id": user.id,
        "spotify_id": user.spotify_id,
        "name": user.name,
        "image_url": user.image_url
    }, HTTPStatus.OK


@blueprint.route("/upload", methods=[HTTPMethod.POST])
@require_auth
def upload() -> ResponseReturnValue:
    user: Optional[User] = user_repository.get_by_spotify_id(session.get(config.SPOTIFY_ID_KEY, ''))
    if not user:
        return {
            "success": False
        }, HTTPStatus.BAD_REQUEST

    file: Optional[FileStorage] = request.files.get("file")
    if not file:
        return {
            "success": False
        }, HTTPStatus.BAD_REQUEST

    if not zipfile.is_zipfile(file.stream):
        return {
            'success': False
        }, HTTPStatus.BAD_REQUEST
    file.stream.seek(0)

    print(file, flush=True)

    return {
        "success": True
    }, HTTPStatus.OK
