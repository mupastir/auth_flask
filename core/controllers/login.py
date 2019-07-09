from uuid import uuid4
from datetime import datetime
from core.schemas.session import SessionSend
from core.schemas.session_details import SessionDetails
from core.controllers.base import Controller
from core.utils.constants import TTL, STATUS_FAILED, STATUS_SUCCESS



class LoginController(Controller):

    def login(self, user_id):
        user, errors = self.user_schema.loads(user_id)
        if not errors:
            return self.create_session(user)
        return self.failed_result()

    def create_session(self, user_info):
        sid = str(uuid4())
        session_details = SessionDetails(user_info, datetime.now())
        session_details_dump, errors = self.session_details_schema.dumps(session_details)
        self.redis_client.set(sid, session_details_dump, ex=TTL)
        session_status = SessionSend(STATUS_SUCCESS)
        return self.session_schema_send.dump(session_status), sid

    def failed_result(self):
        session_status = SessionSend(STATUS_FAILED)
        return self.session_schema_send.dump(session_status)
