from flask import Response

from apprentice.core import format_response, generate_intent_response
from apprentice.helpers import action_ctx


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
