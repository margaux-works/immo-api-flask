from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from schemas import UserSchema, UserUpdateSchema

from db import db
from models.user import UserModel

blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/users")
class UserList(MethodView):
    # Endpoint: GET all users
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()
    
    # Endpoint: POST (create) a new user
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the user.")
        return user

@blp.route("/users/<string:user_id>")
class User(MethodView):
    # Endpoint: GET a single user
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    # Endpoint: PUT (update) user data
    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        user = UserModel.query.get(user_id)

        if not user:
            abort(404, message="User not found.")

        for key, value in user_data.items():
            setattr(user, key, value)

        db.session.commit()
        return user
    