from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionSchema(BaseSchema):
    status = fields.Str()
    sid = fields.UUID()
