import os
from flask import Blueprint, request, jsonify, flash

from .interface import Comment
from .schema import comment_schema, comment_id_schema, comment_update_schema, comment_out_schema

from project.lib.errors import BadRequest

comment_blueprint = Blueprint("comment", __name__)

def add_comment():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = comment_schema.load(request.json)
    comment = Comment.add_comment(data)
    if comment == None:
        raise BadRequest("Comment invalid", 400)
    response = comment_out_schema.dump(comment)
    return response, 200

def comment_by_id():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = comment_id_schema.load(request.json)
    comment = Comment.get_comment(data)
    if comment == None:
        raise BadRequest("Comment invalid", 400)
    response = comment_out_schema.dump(comment)
    return response, 200

def update_comment():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = comment_update_schema.load(request.json)
    comment = Comment.update_comment(data)
    if comment == None:
        raise BadRequest("Comment invalid", 400)
    response = comment_out_schema.dump(comment)
    return response, 200

def delete_comment():
    auth = request.headers.get("Authorization")
    if auth != os.environ.get("AUTH_PASSWORD"):
        raise BadRequest("Authorization invalid", 400)
    data = comment_id_schema.load(request.json)
    delete = Comment.delete_comment(data)
    if delete == False:
        raise BadRequest("Comment invalid", 400)
    return "Comment Deleted!", 200

comment_blueprint.add_url_rule("comment/add_comment", "add_comment", add_comment, methods=["POST"])
comment_blueprint.add_url_rule("comment/comment_by_id", "comment_by_id", comment_by_id, methods=["GET"])
comment_blueprint.add_url_rule("comment/update_comment", "update_comment", update_comment, methods=["POST", "PUT"])
comment_blueprint.add_url_rule("comment/delete_comment", "delete_comment", delete_comment, methods=["DELETE"])