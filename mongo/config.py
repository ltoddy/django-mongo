import os
from ipaddress import ip_address
from socket import INADDR_LOOPBACK

__all__ = ['Config']


class Config:
    # mongo default config
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME') or ''
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD') or ''
    MONGO_HOST = os.environ.get('MONGO_HOST') or ip_address(INADDR_LOOPBACK).compressed
    MONGO_PORT = os.environ.get('MONGO_PORT') or 27017

    def __init__(
            self,
            MONGO_USERNAME: str = None,
            MONGO_PASSWORD: str = None,
            MONGO_HOST: str = None,
            MONGO_PORT: int = None):

        if MONGO_USERNAME is not None: self.MONGO_USERNAME = MONGO_USERNAME
        if MONGO_PASSWORD is not None: self.MONGO_PASSWORD = MONGO_PASSWORD
        if MONGO_HOST is not None: self.MONGO_HOST = MONGO_HOST
        if MONGO_PORT is not None: self.MONGO_PORT = MONGO_PORT

    def mongo_uri(self):
        if self.MONGO_USERNAME and self.MONGO_PASSWORD:
            return f'mongodb://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}/'
        else:
            return f'mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/'


class DevelopmentConfig(Config):
    # TODO
    pass


class TestingConfig(Config):
    # TODO
    pass


class ProductionConfig(Config):
    # TODO
    pass


# TODO
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
