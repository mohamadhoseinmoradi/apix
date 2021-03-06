from apix.resource import apiv1 as api
from apix.resource.apiv1.auth import AuthResource
from apix.resource.apiv1.user import UserResource

api.add_resource(
    AuthResource, "/auth/tokens", methods=["GET", "POST"], endpoint="auth_tokens"
)

api.add_resource(UserResource, "/users", methods=["GET", "POST"], endpoint="users")

api.add_resource(
    UserResource,
    "/users/<user_id>",
    methods=["GET", "PATCH", "PUT", "DELETE"],
    endpoint="user",
)
