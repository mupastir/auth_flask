from core.schemas.base import BaseSchema
from marshmallow import fields


class SessionStatusSchema(BaseSchema):
    status = fields.Str()


class SessionStatusSend:

    def __init__(self, status):
        self.status = status
