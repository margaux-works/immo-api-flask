# Immo REST API – Microservice pour application web de gestion immobilière (Case Study)

Cette API RESTful a été développée dans le cadre d'une étude de cas pour une plateforme de gestion immobilière. Elle permet aux utilisateurs de s'inscrire, se connecter, ajouter et modifier des annonces de biens immobiliers, ainsi que gérer leurs informations personnelles. Chaque utilisateur ne peut modifier que ses propres données et ses propres biens. L'API a été construite en Python avec Flask, et sécurisée via JWT.

## Fonctionnalité

- Inscription et login avec authentification JWT
- Création, consultation et modification de biens immobiliers
- Filtrage des biens par ville
- Modification des info personnelles de l'utilisateur
- Authentication: seul le propriétaire peut modifier ses propres biens
- Documentation de l'API dispo via Swagger UI

---

## Tech utilisées

- Python 3.13+
- Flask
- Flask-Smorest (pour la gestion des routes et documentation OpenAPI)
- Flask-JWT-Extended (authentification JWT)
- Flask-SQLAlchemy (ORM)
- Marshmallow (sérialisation des données)
- Postman (pour tester les routes)
- SQLite (base de données locale)

---

## Lancer le project en local

### 1. Cloner le repo

```bash
git clone https://github.com/your-username/immo-rest-api.git
cd immo-rest-api
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
# OR
.venv\Scripts\activate  # on Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Avant de lancer l'application, créez un fichier `.env` à partir de `.env.example` :

```bash
cp .env.example .env
```

Le fichier `.env` doit contenir :

```env
JWT_SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///data.db
```

> Vous pouvez adapter l'URL de la base si vous utilisez PostgreSQL ou autre.

---

## Lancer le serveur

```bash
flask run
```

Par défaut, l'application est disponible à `http://127.0.0.1:5000`.

### Swagger UI (API Docs)

Accessible ici:

[http://127.0.0.1:5000/swagger-ui](http://127.0.0.1:5000/swagger-ui)

---

## Authentication

Les routes `PUT` et `POST` nécessitent un token JWT.

Pour tester les routes protégées :

1. Inscrivez-vous ou connectez-vous pour obtenir un token via `/register` ou `/login`
2. Ajoutez le token dans l’en-tête de la requête :

```
Authorization: Bearer <your_token_here>
```

---

## Postman Collection

Vous pouvez importer le fichier `postman_collection.json` inclus dans le repo pour tester les endpoints manuellement.

---

## Améliorations potentielles

- Connecter à une vraie base PostgreSQL ou MySQL au lieu de SQLite
- Implémenter des endpoints DELETE pour utilisateurs et biens
- Améliorer la documentation Swagger avec des exemples
- Valider les noms de ville via une API externe

---

## Project Structure

```
.
├── app.py               # App factory
├── db.py                # SQLAlchemy config
├── models/              # SQLAlchemy models
├── resources/           # User & Property blueprints
├── schemas.py           # Marshmallow schemas
├── requirements.txt
└── .env.example         # Environment config template
```
