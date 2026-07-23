import os.path
from typing import Optional
from datetime import datetime
from http import HTTPMethod, HTTPStatus
import zipfile
from flask import Blueprint, session, request
from flask.typing import ResponseReturnValue
from werkzeug.datastructures import FileStorage
from helpers import require_auth
import config
from database_lib.models import User
from database_lib.repositories import user_repository


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

    last_upload_time: Optional[datetime] = user_repository.get_last_upload_time(user.spotify_id)
    if last_upload_time is not None and last_upload_time + config.UPLOAD_TIME_LIMIT > datetime.now():
        print(f"User: '{user.name}' is spamming, bad goy!", flush=True)

        return {
            'success': False
        }, HTTPStatus.FORBIDDEN

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

    try:
        filepath: str = os.path.join(config.UPLOAD_FOLDER, f"{user.id}.zip")

        if os.path.exists(filepath):
            return {
                'success': False
            }, HTTPStatus.BAD_REQUEST

        file.save(filepath)
    except Exception as e:
        print(e, flush=True)

    user_repository.update_upload_time(user.spotify_id)

    return {
        "success": True
    }, HTTPStatus.OK
