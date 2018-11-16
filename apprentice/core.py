import json
import logging

from flask import make_response

logger = logging.getLogger(__name__)


def action_handler():
    def wrapper(func):
        def wrapped(*args, **kwds):
            data = func(*args, **kwds)
            formatted_data = generate_intent_response(data)
            res = format_response(formatted_data)
            return res
        return wrapped
    return wrapper


def format_response(data):
    resp = json.dumps(data, indent=4)
    resp = make_response(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


def generate_intent_response(text, expect_user_response=True):
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