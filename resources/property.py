import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import properties


blp = Blueprint("properties", __name__, description="Operations on properties")

@blp.route("/properties")
class PropertyList(MethodView):
    # Endpoint: GET all properties
    def get(self):
        return {"properties": list(properties.items())}
    
    # Endpoint: POST (create) a new property
    def post(self):
        property_data = request.get_json()
        if "name" not in property_data:
            abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")
        property_id = uuid.uuid4().hex
        property = {**property_data, "id": property_id}
        properties[property_id] = property
        return property, 201


@blp.route("/properties/<string:property_id>")
class Property(MethodView):
    # Endpoint: GET a specific property
    def get(self, property_id):
        try:
            return properties[property_id]
        except KeyError:
            abort(404, message="Property not found")

    # Endpoint: PUT (update) a property
    def put(self, property_id):
        property_data = request.get_json()
        try:
            property = properties[property_id]
        except KeyError:
            abort(404, message="Property not found")

        # Update only provided fields
        for key in ["name", "description", "property_type", "city", "rooms", "owner_id"]:
            if key in property_data:
                property[key] = property_data[key]
        return property, 200


@blp.route("/properties/filter")
class PropertyFilter(MethodView):
    # Endpoint 3: GET (filter) a property by city
    def get(self):
        city = request.args.get("city")
        if not city:
            abort(400, message="Missing city in query parameter")
        filtered = [prop for prop in properties.values() if prop["city"].lower() == city.lower()]
        if not filtered:
            abort(404, message=f"No property currently in {city}")
        return {"Properties": filtered}