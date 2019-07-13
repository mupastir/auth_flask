from core.resources.base import BaseResource
from flask import make_response, request
from core.utils.data_api import AccessToUsers
from core.controllers.login import LoginController
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
