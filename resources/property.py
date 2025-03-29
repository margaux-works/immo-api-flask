from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity



from schemas import PropertySchema, PropertyUpdateSchema

from db import db
from models.property import PropertyModel


blp = Blueprint("properties", __name__, description="Operations on properties")

@blp.route("/properties")
class PropertyList(MethodView):
    # Endpoint: GET all properties
    @blp.response(200, PropertySchema(many=True))
    def get(self):
        return PropertyModel.query.all()
    
    # Endpoint: POST (create) a new property
    @blp.arguments(PropertySchema)
    @blp.response(201, PropertySchema)
    def post(self, property_data):
        property = PropertyModel(**property_data)
        try:
           db.session.add(property)
           db.session.commit()
        except IntegrityError:
           abort(
               400,
               message="A property with that name already exists."
           )
        except SQLAlchemyError:
           abort(500, message="An error occurred while creating the property")
        return property


@blp.route("/properties/<string:property_id>")
class Property(MethodView):
    # Endpoint: GET a specific property
    @blp.response(200, PropertySchema)
    def get(self, property_id):
        property = PropertyModel.query.get_or_404(property_id)
        return property

    # Endpoint: PUT (update) a property
    @blp.arguments(PropertyUpdateSchema)
    @blp.response(200, PropertySchema)
    @jwt_required()
    def put(self, property_data, property_id):
        user_id = get_jwt_identity() 
        property = PropertyModel.query.get(property_id)

        if not property:
            abort(404, message="Property not found.")

        if property.owner_id != int(user_id):
            abort(403, message="You can only update your own properties.")

        for key, value in property_data.items():
            setattr(property, key, value)

        db.session.commit()
        return property


@blp.route("/properties/filter")
class PropertyFilter(MethodView):
    # Endpoint 3: GET (filter) a property by city
    @blp.response(200, PropertySchema(many=True))
    def get(self):
        city = request.args.get("city")
        if not city:
            abort(400, message="Missing city in query parameter")
        filtered = PropertyModel.query.filter(
            PropertyModel.city.ilike(f"%{city}%")
        ).all()
        if not filtered:
            abort(404, message=f"No property currently in {city}")
        return filtered