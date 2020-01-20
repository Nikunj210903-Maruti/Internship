from marshmallow import Schema, fields

class auth_detail(Schema):
    uid=fields.String()
    utoken=fields.String()

class BotData(Schema):
    bot_phone_number = fields.Integer()
    webhook_url = fields.String()
    auth_details = fields.Nested(auth_detail)