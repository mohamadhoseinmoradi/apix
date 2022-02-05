from os import environ


class config:

    DEBUG = environ.get("API_DEBUG", False)
    TESTING = environ.get("API_TESTING", False)
    ENV = environ.get("API_ENV", "production")
