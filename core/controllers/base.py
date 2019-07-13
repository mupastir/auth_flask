from core.schemas.session_status import SessionStatusSchema
from core.schemas.session_details import SessionDetailsSchema
from core.schemas.user import UserSchema
from flask import current_app


class Controller:

    def __init__(self):
        self.session_schema_send = SessionStatusSchema()
        self.session_details_schema = SessionDetailsSchema()
        self.user_schema = UserSchema()
        self.redis_client = current_app.extensions['redis']
