from core.resources.base import BaseResource
from flask import make_response
from core.data_api import AccessToUsers
from core.controllers.login import LoginController
from core.resources.argument_parser import PARSER
from constants import USERNAME


class Login(BaseResource):

    def post(self):
        args = PARSER.parse_args()
        username = args[USERNAME]
        user_id = AccessToUsers.get(username)
        status, sid= LoginController().login(user_id)
        response = make_response(status)
        response.headers.extend({'Session-ID': sid})
        return response
