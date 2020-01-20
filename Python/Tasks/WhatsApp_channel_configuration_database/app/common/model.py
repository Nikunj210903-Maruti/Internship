from flask_restful import fields

auth_data = {
    'uid' : fields.String,
    'utoken' : fields.String
}
model = {
    'bot_phone_number' : fields.Integer,
    'webhook_url' : fields.String,
    'auth_details' : fields.Nested(auth_data)
}
