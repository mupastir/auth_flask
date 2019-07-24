from core.resources.base import BaseResource
from flask import request
from core.utils.data_api import AccessToUsers
from core.controllers.controllers import LoginController, SessionDetailsController
from marshmallow import ValidationError


class Login(BaseResource):

    def post(self):
        data = request.get_json()
        try:
            data = self.login_schema.load(data)
        except ValidationError:
            return 'wrong input data, please try again', 400
        finally:
            user_id = AccessToUsers.post(data['username'], data['password'])
            login_controller = LoginController()
            return login_controller.login(user_id)


class SessionDetails(BaseResource):

    def get(self):
        data = request.get_json()
        try:
            self.session_id_schema.load(data)
        except ValidationError:
            return 'wrong data', 400
        finally:
            sid = data['sid']
            session_details_controller = SessionDetailsController()
            return session_details_controller.get_details(sid)
