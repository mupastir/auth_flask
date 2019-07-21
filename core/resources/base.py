from flask_restful import Resource
from core.schemas.schemas import LoginSchema, SessionIDSchema


class BaseResource(Resource):

    def __init__(self):
        super(BaseResource, self).__init__()
        self.login_schema = LoginSchema()
        self.session_id_schema = SessionIDSchema()
