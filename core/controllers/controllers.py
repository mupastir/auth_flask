from marshmallow import ValidationError
from uuid import uuid4
from datetime import datetime
from core.schemas.schemas import SessionDetails
from core.controllers.base import Controller
from core.constants import TTL


class LoginController(Controller):

    def login(self, user_id):
        user, errors = self.user_schema.loads(user_id)
        if not errors and user:
            return self._create_session(user)
        return 'user does\'nt exist', 400


    def _create_session(self, user_info):
        sid = uuid4()
        session_details = SessionDetails(user_info, datetime.utcnow())
        session_details_dump, errors = self.session_details_schema.dumps(session_details)
        self.redis_client.set(str(sid), session_details_dump, ex=TTL)
        return sid, 200


class SessionDetailsController(Controller):

    def get_details(self, sid):
        session_details = self.get_from_db(sid)
        print(session_details)
        session_details, errors = self.session_details_schema.loads(session_details)
        if session_details and not errors:
            self.expire_session(sid)
            session_details, errors = self.session_details_schema.dump(session_details)
            return session_details, 200
        return f'There does\'nt exist session with this id - {sid}', 400

    def get_from_db(self, sid):
        if self.redis_client.get(sid):
            return self.redis_client.get(sid).decode('utf-8')
        return '{}'

    def expire_session(self, sid):
        self.redis_client.expire(sid, TTL)
