from marshmallow import Schema, fields

class CommentSchema(Schema):
    userid = fields.String(required=True)
    postid = fields.String(required=True)
    body = fields.String(required=True)

class CommentIdSchema(Schema):
    id = fields.String(required=True)

class CommentUpdateSchema(CommentIdSchema):
    body = fields.String(required=True)

class CommentOutSchema(CommentIdSchema, CommentSchema):
    pass

comment_schema = CommentSchema()
comment_id_schema = CommentIdSchema()
comment_update_schema = CommentUpdateSchema()
comment_out_schema = CommentOutSchema()