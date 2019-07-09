from core.schemas.base import BaseSchema
from core.schemas.user import UserSchema
from marshmallow import fields


class SessionDetails:

    def __init__(self, user_info, session_create_date):
        self.user_info = user_info
        self.session_create_date = session_create_date


class SessionDetailsSchema(BaseSchema):

    user_info = fields.Nested(UserSchema)
    session_create_date = fields.DateTime()
