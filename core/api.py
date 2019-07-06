from flask import Blueprint
from flask_restful import Api

from core.resources.login import Login
from core.resources.session_details import SessionDetails

api_auth_blueprint = Blueprint('auth', __name__)
api_auth = Api(api_auth_blueprint)

api_auth.add_resource(Login, '/login')
api_auth.add_resource(SessionDetails, '/sid')
