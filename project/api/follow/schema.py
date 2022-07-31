from marshmallow import Schema, fields

class followSchema(Schema):
    follower_id = fields.String(required=True)
    followed_id = fields.String(required=True)

class followIdSchema(Schema):
    id = fields.String(required=True)

class followOutSchema(followSchema, followIdSchema):
    pass

follow_schema = followSchema()
follow_id_schema = followIdSchema()
follow_out_schema = followOutSchema()