import os
from flask import Blueprint, request, jsonify, flash

from .interface import follow
from .schema import follow_schema, follow_id_schema, follow_out_schema

from project.api.user import user_out_schema

from project.lib.errors import BadRequest

follow_blueprint = Blueprint("follow", __name__)

def follow_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = follow_schema.load(request.json)
    user = follow.follow(data)
    if user == None:
        raise BadRequest("Credentials invalid", 400)
    response = follow_out_schema.dump(user)
    return response, 200

def unfollow_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = follow_id_schema.load(request.json)
    user = follow.unfollow(data)
    if user == False:
        raise BadRequest("Credentials invalid", 400)
    return jsonify("unfollowed!!"), 200

def get_follow():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = follow_id_schema.load(request.json)
    ffollow = follow.get_follow_by_id(data)
    if follow == None:
        raise BadRequest("Credentials invalid", 400)
    response = follow_schema.dump(follow)
    return response, 200

follow_blueprint.add_url_rule("/follow", view_func=follow_user, methods=["POST"])
follow_blueprint.add_url_rule("/unfollow", view_func=unfollow_user, methods=["DELETE"])
follow_blueprint.add_url_rule("/follow_by_id", view_func=get_follow, methods=["GET"])