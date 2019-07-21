from flask import Flask
from flask_redis import FlaskRedis

from core.api import Api
from core.config import runtime_config
from core.resources.smoke import SmokeResource
from core.resources.resources import Login, SessionDetails


app = Flask(__name__)
app.config.from_object(runtime_config())


api = Api(app, prefix='/auth')
api.add_resource(Login, '/login')
api.add_resource(SessionDetails, '/sid')
api.add_resource(SmokeResource, '/smoke')

redis_client = FlaskRedis()
redis_client.init_app(app)
