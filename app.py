
import os 
from dotenv import load_dotenv

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db

from resources.property import blp as PropertyBlueprint
from resources.user import blp as UserBlueprint

load_dotenv()

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret")
    jwt = JWTManager(app)



    with app.app_context():
        import models
        db.create_all()
        

    api.register_blueprint(PropertyBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
