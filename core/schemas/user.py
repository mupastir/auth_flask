from core.schemas.base import BaseSchema
from marshmallow import fields


class UserSchema(BaseSchema):
    id = fields.UUID()
    username = fields.Str()
    email = fields.Str()
    user_address = fields.Str()
    create_user_date = fields.Str()
