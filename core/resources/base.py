from flask_restful import Resource
from core.schemas.login import LoginSchema
from core.schemas.session_id import SessionIDSchema


class BaseResource(Resource):

    def __init__(self):
        self.login_schema = LoginSchema()
        self.session_id_schema = SessionIDSchema()