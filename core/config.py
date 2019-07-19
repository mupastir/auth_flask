import os
import logging
from core.constants import APP_ENV_DEV, APP_ENV_PROD
from deploy_keys import REDIS_PASS


class Config:
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = REDIS_PASS


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig
