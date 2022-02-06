from flask_restx import Resource
from api.controller.apiv1 import userController

class userResource(Resource):

    def get(self, user_id=None):
        """
        GET /users --> get collection of users.
        GET /users/<user_id> --> get single user.
        """
        if user_id == None:
            return userController.get_users()
        else:
            return userController.get_user(user_id)

    def post(self):
        """ 
        POST /users --> create new user.
        """
        return userController.create_user()