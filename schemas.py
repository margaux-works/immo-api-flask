from marshmallow import Schema, fields


# Property Schemas

class RoomSchema(Schema):
    name = fields.Str(required=True)
    size = fields.Int(required=True)

class PropertySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    property_type = fields.Str(required=True)
    city = fields.Str(required=True)
    rooms = fields.List(fields.Nested(RoomSchema), required=True)
    owner_id = fields.Str(required=True)

class PropertyUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    property_type = fields.Str()
    city = fields.Str()
    rooms = fields.List(fields.Nested(RoomSchema))
    owner_id = fields.Str()



# User Schemas

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    birthdate = fields.Date(required=True)  

class UserUpdateSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    birthdate = fields.Date()
