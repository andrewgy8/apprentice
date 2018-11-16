import random
import requests

from apprentice import action_handler


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
