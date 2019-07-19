from flask import Flask, Blueprint
from flask_redis import FlaskRedis
from core.api import Api
from core.config import runtime_config
from core.resources.resources import Login, SessionDetails


app = Flask(__name__)
app.config.from_object(runtime_config())

api_blueprint = Blueprint('auth', __name__)
app.register_blueprint(api_blueprint, url_prefix='/auth')

api = Api(api_blueprint)
api.add_resource(Login, '/login')
api.add_resource(SessionDetails, '/sid')

redis_client = FlaskRedis()
redis_client.init_app(app)
