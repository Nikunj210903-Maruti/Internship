from marshmallow import Schema, fields


class ErrorSchema(Schema):
    ok = fields.Boolean(default=False)
    error = fields.String(default='INTERNAL_SERVER')
    message = fields.Raw()


class DefaultAPIResponseSchema(Schema):
    ok = fields.Boolean(default=True)

