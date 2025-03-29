from db import db
import sqlalchemy # needed for sqlalchemy JSON

class PropertyModel(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    rooms = db.Column(sqlalchemy.JSON, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)



