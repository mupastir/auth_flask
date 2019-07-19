from uuid import uuid4
from datetime import datetime
from core.schemas.schemas import SessionStatusSend, SessionDetails
from core.controllers.base import Controller
from core.constants import TTL, STATUS_FAILED, STATUS_SUCCESS


class LoginController(Controller):

    def login(self, user_id):
        user, errors = self.user_schema.loads(user_id)
        if not errors:
            return self._create_session(user)
        return self._failed_result()

    def _create_session(self, user_info):
        sid = str(uuid4())
        session_details = SessionDetails(user_info, datetime.now())
        session_details_dump, errors = self.session_details_schema.dumps(session_details)
        self.redis_client.set(sid, session_details_dump, ex=TTL)
        session_status = SessionStatusSend(STATUS_SUCCESS)
        return self.session_schema_send.dump(session_status), sid

    def _failed_result(self):
        session_status = SessionStatusSend(STATUS_FAILED)
        return self.session_schema_send.dump(session_status), None


class SessionDetailsController(Controller):

    def get_details(self, sid):
        session_details = self.redis_client.get(sid).decode('utf-8')
        session_details, errors = self.session_details_schema.loads(session_details)
        if not errors:
            session_details, errors = self.session_details_schema.dump(session_details)
            return session_details
        return errors
