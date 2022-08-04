import os
from urllib import response
from flask import Blueprint, request, jsonify

from .interface import Post
from .service import get_likes_on_post
from .schema import post_schema, post_id_schema, post_out_schema

from project.lib.errors import BadRequest

post_blueprint = Blueprint("post", __name__)

def add_post():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = post_schema.load(request.json)
    post = Post.add_post(data)
    response = post_out_schema.dump(post)
    return response, 200

def update_post():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = post_id_schema.load(response.json)
    post = Post.update_post(data)
    if post == None:
        raise BadRequest("Post id invalid", 400)
    response = post_out_schema.dump(post)
    return response, 200

def post_by_id():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = post_id_schema.load(request.json)
    post = Post.post_by_id(data)
    if post == None:
        raise BadRequest("Post id invalid", 400)
    response = post_out_schema.dump(post)
    return response, 200

def likes_on_post():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = post_id_schema.load(request.json)
    users = get_likes_on_post(data)
    if users == None:
        raise BadRequest("Post id invalid", 400)
    return jsonify(users), 200

post_blueprint.add_url_rule("post/add_post", "add_post", add_post, methods=["POST", "PUT"])
post_blueprint.add_url_rule("post/update_post", "update_post", update_post, methods=["POST", "PUT"])
post_blueprint.add_url_rule("post/post_by_id", "post_by_id", post_by_id, methods=["GET"])
post_blueprint.add_url_rule("post/likes_on_post", "likes_on_post", likes_on_post, methods=["GET"])