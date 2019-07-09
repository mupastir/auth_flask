from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionSchema(BaseSchema):
    status = fields.Str()


class SessionSend:

    def __init__(self, status):
        self.status = status
