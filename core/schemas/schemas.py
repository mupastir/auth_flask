from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionDetails:

    def __init__(self, user_information, session_create_date):
        self.user_info = user_information
        self.session_create_date = session_create_date


class SessionStatusSchema(BaseSchema):
    status = fields.Str()


class LoginSchema(BaseSchema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(BaseSchema):
    user_id = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    user_address = fields.Str(required=True)
    create_user_date = fields.Str(required=True)


class SessionIDSchema(BaseSchema):
    sid = fields.Str()
    user_info = fields.Nested(UserSchema)


class SessionDetailsSchema(BaseSchema):
    user_info = fields.Nested(UserSchema)
    session_create_date = fields.Date()

