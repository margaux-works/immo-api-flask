from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)

    properties = db.relationship("PropertyModel", back_populates="user", lazy="dynamic")

    
