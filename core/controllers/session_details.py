from core.controllers.base import Controller


class SessionDetailsController(Controller):

    def get_details(self, sid):
        session_details = self.redis_client.get(sid).decode('utf-8')
        session_details, errors = self.session_details_schema.loads(session_details)
        if not errors:
            session_details, errors = self.session_details_schema.dump(session_details)
            return session_details
        return errors
