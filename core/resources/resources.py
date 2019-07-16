from core.resources.base import BaseResource
from flask import make_response, request
from core.utils.data_api import AccessToUsers
from core.controllers.controllers import LoginController, SessionDetailsController
from marshmallow import ValidationError


class Login(BaseResource):

    def post(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
            user_id = AccessToUsers.get(data['username'], data['password'])
            status, sid = LoginController().login(user_id)
            response = make_response(status)
            response.headers.extend({'Session-ID': sid})
            return response
        except ValidationError:
            return 500


class SessionDetails(BaseResource):

    def get(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
            sid = data['sid']
            session_details = SessionDetailsController().get_details(sid)
            response = make_response(session_details)
            response.headers.extend({'Session-ID': sid})
            return response
        except ValidationError:
            return 500
