import os
import logging

from core.constants import APP_ENV_DEV, APP_ENV_PROD


class Config:
    REDIS_HOST = os.environ.get('DB_HOST', 'localhost')
    REDIS_PORT = os.environ.get('DB_PORT', 6379)
    REDIS_DB = os.environ.get('DEFAULT_DB', 0)
    REDIS_PASSWORD = os.environ.get('DB_PASSWORD', 'redis')
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)
    REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig
