from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import jwt_required, get_jwt_identity


from db import db
from models.user import UserModel
from schemas import UserSchema, UserUpdateSchema, UserLoginSchema


blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/users")
class UserList(MethodView):
    # Endpoint: GET all users
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


@blp.route("/users/<int:user_id>")
class User(MethodView):
    # Endpoint: GET a single user
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    # Endpoint: PUT (update) user data
    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    @jwt_required()
    def put(self, user_data, user_id):
        user = UserModel.query.get_or_404(user_id)

        # get ID of currently logged-in user with JWT token
        current_user_id = get_jwt_identity()

        # prevents user from editing another user's data
        if int(current_user_id) != user_id:
            abort(403, message="You can only update your own user data.")
                  
        for key, value in user_data.items():
            setattr(user, key, value)

        db.session.commit()
        return user

# User Authentication - Register & Login
    
@blp.route("/register")
class UserRegister(MethodView):
    # Endpoint: POST (create/register) a new user 
    @blp.arguments(UserSchema)
    def post(self, user_data):
        # check if username already exists to prevent duplicates
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]), # hash user's password
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            birthdate=user_data.get("birthdate")
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201
    
@blp.route("/login")
class UserLogin(MethodView):
    # Endpoint: POST Login as an existing user
    @blp.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id))
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")