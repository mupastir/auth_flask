from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionIDSchema(BaseSchema):
    sid = fields.Str()
