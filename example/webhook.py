import random

import requests

from apprentice import format_response, generate_intent_response


def cool_fact_generator(*args, **kwargs):
    data = _fact_response()
    formatted_data = generate_intent_response(data)
    return format_response(formatted_data)


def _fact_response():
    res = requests.get('https://history.muffinlabs.com/date')
    data = res.json().get('data')

    fact = random.choice(data['Events'])
    year = fact['year']
    text = fact['text']
    phrase = f'Today, in the year {year} {text}'
    return phrase
