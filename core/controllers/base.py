from core.schemas.schemas import SessionStatusSchema, SessionDetailsSchema, UserSchema
from flask import current_app


class Controller:

    def __init__(self):
        self.session_schema_send = SessionStatusSchema()
        self.session_details_schema = SessionDetailsSchema()
        self.user_schema = UserSchema()
        self.redis_client = current_app.extensions['redis']
