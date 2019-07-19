import os
import logging
from core.constants import APP_ENV_DEV, APP_ENV_PROD


class Config:
    REDIS_HOST = os.environ.get('DB_HOST', 'localhost')
    REDIS_PORT = os.environ.get('DB_PORT', 6379)
    REDIS_DB = os.environ.get('DEFAULT_DB', 0)
    REDIS_PASSWORD = os.environ.get('DB_PASSWORD', 'redis')
    DEBUG = False
    LOG_LEVEL = logging.INFO
    REDIS_URI = 'redis://:{password}@{host}:{port}/{db_name}'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig
