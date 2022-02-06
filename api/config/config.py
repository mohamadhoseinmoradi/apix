from os import environ

class config:

    DEBUG = bool(environ.get("API_DEBUG", False))
    TESTING = bool(environ.get("API_TESTING", False))
    ENV = environ.get("API_ENV", "production")
    SECRET = environ.get("API_SECRET", "HARD-DEV-SECRET")
    SQLALCHEMY_DATABASE_URI = environ.get("API_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG 
    JWT_TOKEN_LIFETIME = int(environ.get("API_JWT_TOKEN_LIFETIME", 100))
    JWT_ALGO = environ.get("API_JWT_ALGO", "HS512")

