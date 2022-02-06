from flask import Flask, Blueprint
from flask_restx import Api
from api import resource
from api.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1",__name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)
    app.register_blueprint(apiv1_bp) # register /api/v1 to application.
    return app
