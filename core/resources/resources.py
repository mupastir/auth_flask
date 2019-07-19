from core.resources.base import BaseResource
from flask import request
from core.utils.data_api import AccessToUsers
from core.controllers.controllers import LoginController, SessionDetailsController
from marshmallow import ValidationError


class Login(BaseResource):

    def post(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
        except ValidationError:
            return {
                'Status': 'failed'
            }, 300
        finally:
            user_id = AccessToUsers.get(data['username'], data['password'])
            status, sid = LoginController().login(user_id)
            return {
                       'Status': status,
                       'Session-ID': sid
                   }, 200


class SessionDetails(BaseResource):

    def get(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
        except ValidationError:
            return {
                       'Status': 'failed'
                   }, 300
        finally:
            sid = data['sid']
            session_details = SessionDetailsController().get_details(sid)
            return session_details, 200
