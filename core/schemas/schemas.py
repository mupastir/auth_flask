from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionDetails:

    def __init__(self, user_information, session_create_date):
        self.user_info = user_information
        self.session_create_date = session_create_date


class SessionStatusSchema(BaseSchema):
    status = fields.Str()


class LoginSchema(BaseSchema):
    username = fields.Str()
    password = fields.Str()


class UserSchema(BaseSchema):
    user_id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    user_address = fields.Str()
    create_user_date = fields.Str()


class SessionIDSchema(BaseSchema):
    sid = fields.Str()
    user_info = fields.Nested(UserSchema)


class SessionDetailsSchema(BaseSchema):
    user_info = fields.Nested(UserSchema)
    session_create_date = fields.Date()

