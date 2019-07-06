from core.schemas.session import SessionSchema
from core.schemas.user import UserSchema
from flask import current_app


class Controller:

    def __init__(self):
        self.schema_send = SessionSchema()
        self.user_schema = UserSchema()
        self.redis_client = current_app.extensions['redis']
