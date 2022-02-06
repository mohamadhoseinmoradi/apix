from shared import uuidgen
from api import db

class User(db.Model):

    id = db.column(db.string(64), primary_key=True, default=uuidgen)
    username = db.column(db.string(128), unique=True, index=True, nullable=False)
    password = db.column(db.string(128), nullable=False)