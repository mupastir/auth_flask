from flask import Flask
from core.api import api_auth_blueprint
from flask_redis import FlaskRedis
from core.config import runtime_config


app = Flask(__name__)
app.config.from_object(runtime_config())
app.register_blueprint(api_auth_blueprint,  url_prefix='/auth')
redis_client = FlaskRedis()
redis_client.init_app(app)
