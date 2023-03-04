from marshmallow import fields, Schema, validate

VALID_CMD_COMMANDS = ('filter' 'unique', 'limit', 'map', 'sort')


class RequestSchema (Schema):
    cmd1 = fields. Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value1 = fields. Str(required=True)
    cmd2 = fields. Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value2 = fields. Str(required=True)
    file_name = fields. Str(required=True)