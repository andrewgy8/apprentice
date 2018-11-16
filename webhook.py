import json
import logging
import random

from flask import make_response
import requests

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


@action_handler()
def cool_fact_generator(*args, **kwargs):
    return _fact_response()


def _fact_response():
    res = requests.get('https://history.muffinlabs.com/date')
    data = res.json().get('data')

    fact = random.choice(data['Events'])
    year = fact['year']
    text = fact['text']
    phrase = f'Today, in the year {year} {text}'
    return phrase


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