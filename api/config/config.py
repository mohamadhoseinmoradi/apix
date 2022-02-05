from os import environ


class config:

    DEBUG = bool(environ.get("API_DEBUG", False))
    TESTING = bool(environ.get("API_TESTING", False))
    ENV = environ.get("API_ENV", "production")
