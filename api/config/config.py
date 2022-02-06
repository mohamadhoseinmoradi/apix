from os import environ


class config:

    DEBUG = bool(environ.get("API_DEBUG", False))
    TESTING = bool(environ.get("API_TESTING", False))
    ENV = environ.get("API_ENV", "production")
    SQLALCHEMY_DATABASE_URI =  environ.get("API_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG 