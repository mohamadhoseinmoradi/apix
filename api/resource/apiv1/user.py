from flask_restx import Resource
from api.controller.apiv1 import UserController

class userResource(Resource):

    def get(self, user_id=None):
        """
        GET /users --> get collection of users.
        GET /users/<user_id> --> get single user.
        """
        if user_id == None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)

    def post(self):
        """ 
        POST /users --> create new user.
        """
        return UserController.create_user()