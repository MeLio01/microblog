from marshmallow import Schema, fields

class likeSchema(Schema):
    userid = fields.String(required=True)
    postid = fields.String(required=True)

like_schema = likeSchema()