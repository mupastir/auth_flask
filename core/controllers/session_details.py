from core.controllers.base import Controller


class SessionDetailsController(Controller):

    def get_details(self, sid):
        session_details = self.redis_client.get(str(sid))
        if session_details:
            return {'status': 'logged in'}
        return {'status': 'failed', 'desc': 'session doesn\'t exists', 'sid': sid}
