from flask import Flask
from flask_redis import FlaskRedis
from core.api import api_auth_blueprint
from fakeredis import FakeRedis
from deploy_keys import REDIS_PASS


class FlaskConfig:
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = REDIS_PASS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object(FlaskConfig)
        redis_client = FlaskRedis()
    else:
        app.config.update(test_config)
        redis_client = FlaskRedis.from_custom_provider(FakeRedis)

    app.register_blueprint(api_auth_blueprint,  url_prefix='/auth')
    redis_client.init_app(app)
    return app

