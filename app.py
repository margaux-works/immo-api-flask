from flask import Flask, request

app = Flask(__name__)

## STATIC DATA
properties = [
    {
        "name": "Loft Parisien",
        "description": "Appartement lumineux dans le Marais",
        "property_type": "Appartement",
        "city": "Paris",
        "rooms": [
            {"name": "Salon", "size": 20},
            {"name": "Chambre", "size": 15}
        ],
        "owner_id": 1
    },
    {
        "name": "Maison Bord de Mer",
        "description": "Maison avec vue sur la mer à Marseille",
        "property_type": "Maison",
        "city": "Marseille",
        "rooms": [
            {"name": "Salon", "size": 30},
            {"name": "Cuisine", "size": 10},
            {"name": "Chambre", "size": 25}
        ],
        "owner_id": 2
    },
    {
        "name": "Studio Central",
        "description": "Studio confortable au centre de Lyon",
        "property_type": "Studio",
        "city": "Lyon",
        "rooms": [
            {"name": "Pièce principale", "size": 18}
        ],
        "owner_id": 3
    }
]

users = [
    {
        "id": 1,
        "first_name": "Jodie",
        "last_name": "Dupont",
        "birthdate": "1990-05-12"
    },
    {
        "id": 2,
        "first_name": "Kirsten",
        "last_name": "Doe",
        "birthdate": "1985-08-30"
    },
    {
        "id": 3,
        "first_name": "Elliot",
        "last_name": "Smith",
        "birthdate": "1972-11-22"
    }
]

## PROPERTY ENDPOINTS
# Endpoint 1: GET all properties
@app.get("/properties")
def get_all_properties():
    return {"properties": properties}

#Endpoint 2: GET a specific property
@app.get("/properties/<string:name>")
def get_property(name):
    for property in properties:
        if property["name"] == name:
            return property
    return {"message": "property not found"}, 404

# Endpoint 3: GET (filter) a property by city
@app.get("/properties/filter")
def filter_property():
    city = request.args.get("city")
    filtered = [ prop for prop in properties if prop["city"].lower() == city.lower()]
    if filtered:
        return {"properties": filtered}, 201
    else:
        return {"message": f"no property found in {city}"}, 404

# Endpoint 4: POST (create) a new property
@app.post("/properties")
def add_property():
    request_data = request.get_json()
    new_property = {"name": request_data["name"], "description": request_data["description"], "property_type": request_data["property_type"], "city": request_data["city"], "rooms": request_data["rooms"], "owner_id": request_data["owner_id"]}
    properties.append(new_property)
    return new_property, 201

#Endpoint 5: PUT (update) a property
@app.put("/properties/<string:name>")
def update_property(name):
    request_data = request.get_json()

    for property in properties:
        if property["name"] == name:
            #update each field only if provided
            if "name" in request_data:
                property["name"] = request_data["name"]
            if "description" in request_data:
                property["description"] = request_data["description"]
            if "property_type" in request_data:
                property["property_type"] = request_data["property_type"]
            if "city" in request_data:
                property["city"] = request_data["city"]
            if "owner_id" in request_data:
                property["owner_id"] = request_data["owner_id"]
            if "rooms" in request_data:
                property["rooms"] = request_data["rooms"]

            return property, 200
        
    return {"message": "property not found"}, 404


## USER ENDPOINTS
# Endpoint 1: GET all users
@app.get("/users")
def get_all_users():
    return {"users": users}

# Endpoint 2: GET a single user
@app.get("/users/<int:id>")
def get_single_user(id):
    for user in users:
        if user["id"] == id:
            return user
    return {"message": f"no user found with id {id}"}, 404

# Endpoint 3: PUT (update) user data
@app.put("/users/<int:id>")
def update_user(id):
    request_data = request.get_json()

    for user in users:
        if user["id"] == id:
            #update each field only if provided
            if "first_name" in request_data:
                user["first_name"] = request_data["first_name"]
            if "last_name" in request_data:
                user["last_name"] = request_data["last_name"]
            if "birthdate" in request_data:
                user["birthdate"] = request_data["birthdate"]
            return user, 200
        
    return {"message": "user not found"}, 404