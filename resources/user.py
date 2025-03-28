from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import UserSchema, UserUpdateSchema
from db import users

blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/users")
class UserList(MethodView):
    # Endpoint: GET all users
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return list(users.values())

@blp.route("/users/<string:id>")
class User(MethodView):
    # Endpoint: GET a single user
    @blp.response(200, UserSchema)
    def get(self, id):
        try:
            return users[id]
        except KeyError:
            abort(404, message="User not found")

    # Endpoint: PUT (update) user data
    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, id):
        user = users.get(id)
        if not user:
            abort(400, message="User not found")
        for key in ["first_name", "last_name", "birthdate"]:
            if key in user_data:
                user[key] = user_data[key]
        return user