from uuid import uuid4
from datetime import datetime
from core.schemas.session_details import SessionDetails
from core.controllers.base import Controller
from constants import TTL, STATUS_FAILED, STATUS_SUCCESS


class LoginController(Controller):

    def login(self, username, user_id):
        user, errors = self.user_schema.load(user_id)
        if not errors:
            result_send = self.create_session(username, user)
            return result_send
        return self.failed_result()

    def create_session(self, username, user):
        sid = uuid4()
        session_details_redis = username + ',' + str(user) + ',' + str(datetime.now())
        self.redis_client.set(str(sid), session_details_redis, ex=TTL)
        send_session_details = SessionDetails(STATUS_SUCCESS, sid, user_id=user)
        return self.schema_send.dump(send_session_details)

    def failed_result(self):
        send_session_details = SessionDetails(STATUS_FAILED, None, None)
        result_send = self.schema_send.dump(send_session_details)
        return result_send
