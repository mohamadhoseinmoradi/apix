from apix import ma
from apix.model import User

class UserSchema(ma.SQLAlchemySchema):
    class meta:
        model = User 

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.auto_field(load_only=True)