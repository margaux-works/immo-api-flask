
from datetime import date

users = {
    'f1a2b3': {
        'first_name': 'Jodie Laura', 
        'last_name': 'Dupont', 
        'birthdate': date(1990, 5, 12)
        }, 
        'a4b5c6': {
            'first_name': 'Kirsten', 
            'last_name': 'Doe', 
            'birthdate': date(1979, 7, 11)
        }, 
        'x7y8z9': {
            'first_name': 'Elliot', 
            'last_name': 'Smith', 
            'birthdate': date(1953, 9, 20)
        }
    }

properties = {
    'cd28cb68a200409ba3c498a614305871': {
        'name': 'Loft Parisien', 
        'description': 'Appartement lumineux dans le Marais', 
        'property_type': 'Appartement', 
        'city': 'Paris', 
        'rooms': [
            {'name': 'Salon', 'size': 20}, 
            {'name': 'Chambre', 'size': 15}
        ], 
        'id': 'cd28cb68a200409ba3c498a614305871',
        'owner_id': 'f1a2b3'
    
    }, 
    '0fb1447586054759b54184af9fa1128d': {
        'name': 'Maison Bord de Mer', 
        'description': 'Maison avec vue sur la mer à Marseille', 
        'property_type': 'Maison', 
        'city': 'Marseille', 
        'rooms': [
            {'name': 'Salon', 'size': 30}, 
            {'name': 'Cuisine', 'size': 10}, 
            {'name': 'Chambre', 'size': 25}
        ], 
        'id': '0fb1447586054759b54184af9fa1128d',
        'owner_id': 'a4b5c6'
    }, 
    '6d1e533b368947019dfae8d7f0b71164': {
        'name': 'Studio Central', 
        'description': 'Studio confortable au centre de Lyon', 
        'property_type': 'Studio', 
        'city': 'Lyon', 
        'rooms': [
             {'name': 'Pièce principale', 'size': 18}
        ], 
        'id': '6d1e533b368947019dfae8d7f0b71164',
        'owner_id': 'x7y8z9'
    }
}
