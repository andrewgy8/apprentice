import json

from flask import Flask, make_response

from marshmallow import Schema, fields


def response(data):
    resp = json.dumps(data, indent=4)
    resp = make_response(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


def intent_response(text, expect_user_response=True):
    return {
        'speech': text,
        'displayText': None,
        'messages': [
            {
                "type": 0,
                "speech": text
            }
        ],
        'data': {
            'google': {
                "expect_user_response": expect_user_response,
                "is_ssml": True,
                "permissions_request": None,
            }
        },
        'contextOut': [],
        'source': 'webhook'
    }


class Apprentice(Flask):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.flask = Flask(__name__)
        super().__init__(__name__, *args, **kwargs)

    def action(self, route='/'):
        def decorator(function):
            @self.flask.route(route, methods=['POST', 'GET'])
            def wrapper(*args, **kwargs):
                return function(*args, **kwargs)

            return wrapper

        return decorator

    def response(self, reply):
        res = intent_response(reply)
        return response(res)


class MessageSchema(Schema):
    type = fields.Int()
    speech = fields.Str()


class ResponseSchema(Schema):
    expect_user_response = fields.Bool()


class UserSchema(Schema):
    expect_user_response = fields.Bool()
    is_ssml = fields.Bool()
    permissions_request = fields.Bool()


class MetaSchema(Schema):
    google = fields.Nested()


class IntentSchema(Schema):
    speech = fields.Str()
    displayText = fields.Str()
    messages = fields.Nested(MessageSchema, many=True)
    data = fields.Nested(MetaSchema)
    contextOut = fields.Str()
    source = 'webhook'
