from marshmallow import Schema, fields



# Plain schemas 
class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    birthdate = fields.Date(required=True)


class RoomSchema(Schema):
    name = fields.Str(required=True)
    size = fields.Float(required=True)


class PlainPropertySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    property_type = fields.Str(required=True)
    city = fields.Str(required=True)
    rooms = fields.List(fields.Nested(RoomSchema()), required=True)


# Schemas with nested relationships
class PropertySchema(PlainPropertySchema):
    owner_id = fields.Int(required=True, load_only=True)
    owner = fields.Nested(PlainUserSchema(), dump_only=True)


class UserSchema(PlainUserSchema):
    properties = fields.List(fields.Nested(PlainPropertySchema()), dump_only=True)



# Update schemas
class PropertyUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    property_type = fields.Str()
    city = fields.Str()
    rooms = fields.List(fields.Nested(RoomSchema()))
    owner_id = fields.Int()


class UserUpdateSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    birthdate = fields.Date()
