import os
from flask import Blueprint, request, jsonify, flash

from project.api import user

from .interface import User
from .schema import user_profile_schema, user_id_schema, user_out_schema, user_email_schema, user_update_schema

from project.lib.errors import BadRequest

user_blueprint = Blueprint("user", __name__)

def register_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_profile_schema.load(request.json)
    user = User.add_user(data)
    response = user_out_schema.dump(user)
    return response, 200

def user_by_username():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_profile_schema.load(request.json)
    user = User.get_user_by_username(data)
    if user == None:
        raise BadRequest("Username invalid", 400)
    response = user_out_schema.dump(user)
    return response, 200

def user_by_email():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_email_schema.load(request.json)
    user = User.get_user_by_email(data)
    if user == None:    
        raise BadRequest("Email invalid", 400)
    response = user_out_schema.dump(user)
    return response, 200

def update_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_update_schema.load(request.json)
    user = User.update_user(data)
    if user == None:
        raise BadRequest("Credentials invalid", 400)
    response = user_out_schema.dump(user)
    return response, 200

def delete_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_id_schema.load(request.json)
    delete = User.delete_user(data)
    if delete == False:
        raise BadRequest("Credentials invalid", 400)
    return jsonify("deleted!!"), 200

def posts_by_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_id_schema.load(request.json)
    posts = User.posts_by_user(data)
    if posts == None:
        raise BadRequest("No posts by user", 400)
    return jsonify(posts), 200

def followed_by_user():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = user_id_schema.load(request.json)
    users = User.get_followed(data)
    if users == None:
        raise BadRequest("No users followed by user", 400)
    return jsonify(users), 200 

user_blueprint.add_url_rule("user/register_user", "register_user", register_user, methods=["POST"])
user_blueprint.add_url_rule("user/user_by_username", "user_by_username", user_by_username, methods=["GET"])
user_blueprint.add_url_rule("user/user_by_email", "user_by_email", user_by_email, methods=["GET"])
user_blueprint.add_url_rule("user/update_user", "update_user", update_user, methods=["POST", "PUT"])
user_blueprint.add_url_rule("user/posts_by_user", "posts_by_user", posts_by_user, methods=["GET"])
user_blueprint.add_url_rule("user/following_by_user", "following_by_user", followed_by_user, methods=["GET"])
user_blueprint.add_url_rule("user/delete_user", "delete_user", delete_user, methods=["DELETE"])