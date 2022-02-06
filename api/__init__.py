from flask import Flask, Blueprint
from flask_restx import Api
from api import resource
import sqlalchemy
from api.config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
apiv1_bp = Blueprint("apiv1",__name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    db.init_app()
    app.config.from_object(config)
    app.register_blueprint(apiv1_bp) # register /api/v1 to application.
    return app
