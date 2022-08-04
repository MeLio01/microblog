import os
from flask import Blueprint, request, jsonify, flash

from .interface import like
from .schema import like_schema

from project.lib.errors import BadRequest

like_blueprint = Blueprint("like", __name__)

def like_post():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = like_schema.load(request.json)
    like_ = like.add_like(data)
    if like_ == None:
        raise BadRequest("Credentials invalid", 400)
    response = like_schema.dump(like_)
    return response, 200

def unlike_post():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = like_schema.load(request.json)
    unlike_ = like.delete_like(data)
    if unlike_ == False:
        raise BadRequest("Credentials invalid", 400)
    return jsonify("unliked!!"), 200

like_blueprint.add_url_rule("/like", view_func=like_post, methods=["POST"])
like_blueprint.add_url_rule("/unlike", view_func=unlike_post, methods=["DELETE"])