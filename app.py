from flask import Flask

app = Flask(__name__)

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

# Endpoint 1: GET all properties
@app.get("/properties")
def get_properties():
    return {"properties": properties}
