from crypt import methods
from api.resource import apiv1 as api
from api.resource.apiv1.user import userResource
from api.resource.apiv1.auth import AuthResource

api.add_resource(
    AuthResource,
    "/auth/tokens"
    methods=["GET", "POST"]
    endpoint="auth_tokens"
)

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