# resources/user.py
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import users

blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/users")
class UserList(MethodView):
    # Endpoint: GET all users
    def get(self):
        return {"users": list(users.items())}


@blp.route("/users/<string:id>")
class User(MethodView):
    # Endpoint: GET a single user
    def get(self, id):
        try:
            return users[id]
        except KeyError:
            abort(404, message="User not found")

    # Endpoint: PUT (update) user data
    def put(self, id):
        user = users.get(id)
        if not user:
            abort(400, message="User not found")
        user_data = request.get_json()
        for key in ["first_name", "last_name", "birthdate"]:
            if key in user_data:
                user[key] = user_data[key]
        return user, 200