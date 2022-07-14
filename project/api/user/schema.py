from marshmallow import Schema, fields

class UserProfileSchema(Schema):
    username = fields.String(required=True)
    email = fields.String()
    password_hash = fields.String()

class UserEmailSchema(Schema):
    email = fields.String(required=True)

class UserIdSchema(Schema):
    id = fields.String(required=True)

class UserUpdateSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()
    about_me = fields.String()

class UserOutSchema(UserProfileSchema, UserIdSchema):
    about_me = fields.String()
    last_seen = fields.String()

user_profile_schema = UserProfileSchema()
user_email_schema = UserEmailSchema()
user_id_schema = UserIdSchema()
user_update_schema = UserUpdateSchema()
user_out_schema = UserOutSchema()