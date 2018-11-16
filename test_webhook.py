import pytest
import responses
from flask import Flask, Response

from webhook import _fact_response, cool_fact_generator, generate_intent_response, format_response


@pytest.fixture(autouse=True)
def api_response(historical_fact_response):
    return responses.add(
        responses.GET,
        'https://history.muffinlabs.com/date',
        json=historical_fact_response,
        status=200)


def action_ctx(function):
    def wrap_function(*args, **kwargs):
        flask_app = Flask(__name__)
        with flask_app.test_request_context():
            return function(*args, **kwargs)
    return wrap_function


class TestCoolFactGenerator:

    @action_ctx
    def test_returns_response_with_json_when_called(self):
        request = {}
        res = cool_fact_generator(request)

        assert res.json == {
            'contextOut': [],
            'data': {
                'google': {
                    'expect_user_response': True,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'displayText': None,
            'messages': [{
                'speech': 'Today, in the year 308 At Carnuntum, Emperor '
                          'emeritus Diocletian confers with Galerius, Augustus '
                          'of the East, and Maximianus, the recently returned '
                          'former Augustus of the West, in an attempt to end '
                          'the civil wars of the Tetrarchy.',
                'type': 0
            }],
            'source': 'webhook',
            'speech': 'Today, in the year 308 At Carnuntum, Emperor '
                      'emeritus Diocletian confers with Galerius, Augustus '
                      'of the East, and Maximianus, the recently returned '
                      'former Augustus of the West, in an attempt to end '
                      'the civil wars of the Tetrarchy.'
        }

    @action_ctx
    def test_returns_content_type_json_when_called(self):
        request = {}
        res = cool_fact_generator(request)

        assert res.headers['Content-Type'] == 'application/json'


class TestFactResponse:

    def test_returns_structured_json_object(self):
        res = _fact_response()

        assert res == 'Today, in the year 308 At Carnuntum, Emperor ' \
                      'emeritus Diocletian confers with Galerius, Augustus ' \
                      'of the East, and Maximianus, the recently returned ' \
                      'former Augustus of the West, in an attempt to end ' \
                      'the civil wars of the Tetrarchy.'


class TestGenerateIntentResponse:

    def test_returns_object_when_given_text(self):
        text = 'Hello world'
        json_response = generate_intent_response(text)

        assert json_response == {
            'contextOut': [],
            'data': {
                'google': {
                    'expect_user_response': True,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'displayText': None,
            'messages': [{
                'speech': 'Hello world',
                'type': 0
            }],
            'source': 'webhook',
            'speech': 'Hello world'
        }

    def test_returns_expect_user_response_when_set_to_false(self):
        text = 'Hello world'
        json_response = generate_intent_response(text,
                                                 expect_user_response=False)

        assert json_response == {
            'contextOut': [],
            'data': {
                'google': {
                    'expect_user_response': False,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'displayText': None,
            'messages': [{
                'speech': 'Hello world',
                'type': 0
            }],
            'source': 'webhook',
            'speech': 'Hello world'
        }


class TestFormatResponse:

    @action_ctx
    def test_returns_flask_response_object_when_called(self):
        data = {'msg': 'hello world'}
        res = format_response(data)

        assert isinstance(res, Response)
        assert res.json == data
        assert res.headers['Content-Type'] == 'application/json'
