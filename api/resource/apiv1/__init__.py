from crypt import methods
from api import apiv1 as api
from api.resource.apiv1.user import userResource

api.add_resource(
    userResource,
    "/users",
    methods=["GET","POST"],
    endpoint="users"
)

api.add_resource(
    userResource,
    "/users/<user_id>",
    methods=["GET", "PATCH", "PUT", "DELETE"],
    endpoint="user"
)