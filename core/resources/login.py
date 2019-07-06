from core.resources.base import BaseResource
from core.data_api import AccessToUsers
from core.controllers.login import LoginController
from core.resources.argument_parser import PARSER
from constants import USERNAME


class Login(BaseResource):

    def post(self):
        args = PARSER.parse_args()
        username = args[USERNAME]
        user_id = AccessToUsers.get(username)
        login_controller = LoginController()
        return login_controller.login(username, user_id)
