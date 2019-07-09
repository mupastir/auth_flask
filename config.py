from flask import Flask
from flask_redis import FlaskRedis
from core.api import api_auth_blueprint
from deploy_keys import REDIS_PASS


class FlaskConfig:
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = REDIS_PASS
    # REDIS_URL = "redis://:redis@localhost:6379/0"


def create_app():
    app = Flask(__name__)
    redis_client = FlaskRedis()
    app.config.from_object(FlaskConfig)
    app.register_blueprint(api_auth_blueprint,  url_prefix='/auth')
    redis_client.init_app(app)
    return app

