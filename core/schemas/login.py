from core.schemas.base import BaseSchema
from marshmallow import fields


class LoginSchema(BaseSchema):
    username = fields.Str()
    password = fields.Str()
