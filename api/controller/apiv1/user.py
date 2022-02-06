from api.model import user


class userController():

    def get_users():
        return user
    
    def get_user(user_id):
        return user[int(user_id)]