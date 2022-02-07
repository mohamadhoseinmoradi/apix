from os import environ

class Config:

    DEBUG = bool(environ.get("APIX_DEBUG", False))
    TESTING = bool(environ.get("APIX_TESTING", False))
    ENV = environ.get("APIX_ENV", "production")
    SECRET = environ.get("APIX_SECRET", "HARD-DEV-SECRET")
    SQLALCHEMY_DATABASE_URI = environ.get("APIX_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG 
    JWT_TOKEN_LIFETIME = int(environ.get("APIX_JWT_TOKEN_LIFETIME", 100))
    JWT_ALGO = environ.get("APIX_JWT_ALGO", "HS512")

