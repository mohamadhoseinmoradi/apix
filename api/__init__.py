from flask import Flask
from api.config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    return app
