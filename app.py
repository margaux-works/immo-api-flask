import uuid
from flask import Flask, request
from flask_smorest import Api, abort
from db import properties, users

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Immo REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

## PROPERTY ENDPOINTS
# Endpoint 1: GET all properties
@app.get("/properties")
def get_all_properties():
    return {"properties": list(properties.items())}

#Endpoint 2: GET a specific property
@app.get("/properties/<string:property_id>")
def get_property(property_id):
    try:
        return properties[property_id]
    except KeyError:
        print(abort.__module__)
        abort(404, message="Property not found")

# Endpoint 3: GET (filter) a property by city
@app.get("/properties/filter")
def filter_property_by_city():
    city = request.args.get("city")
    if not city:
        abort(400, message="Missing city in query parameter")
    filtered = [prop for prop in properties.values() if prop["city"].lower() == city.lower()]
    if not filtered:
        abort(404, message=f"No property currently in {city}")
    return {"Properties" : filtered}

# Endpoint 4: POST (create) a new property
@app.post("/properties")
def add_property():
    property_data = request.get_json()

    if "name" not in property_data:
        abort(
            400,
            message="Bad request. Ensure 'name' is included in the JSON payload.",
        )
    property_id = uuid.uuid4().hex
    property = {**property_data, "id": property_id}
    properties[property_id] = property
    return property, 201

#Endpoint 5: PUT (update) a property
@app.put("/properties/<string:property_id>")
def update_property(property_id):
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
        

## USER ENDPOINTS
# Endpoint 1: GET all users
@app.get("/users")
def get_all_users():
    return {"users": list(users.items())}

# Endpoint 2: GET a single user
@app.get("/users/<string:id>")
def get_single_user(id):
    try:
        return users[id]
    except KeyError:
        abort(404, message="User not found")

# Endpoint 3: PUT (update) user data
@app.put("/users/<string:id>")
def update_user(id):
    user = users.get(id)
    if not user:
        abort(400, message="User not found")
    user_data = request.get_json()
    for key in ["first_name", "last_name", "birthdate"]:
        if key in user_data:
            user[key] = user_data[key]
    return user, 200