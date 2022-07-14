from marshmallow import Schema, fields

class PostSchema(Schema):
    user_id = fields.String(required=True)
    body = fields.String()

class PostIdSchema(Schema):
    id = fields.String(required=True)

class PostOutSchema(PostSchema, PostIdSchema):
    pass

post_schema = PostSchema()
post_id_schema = PostIdSchema()
post_out_schema = PostOutSchema()