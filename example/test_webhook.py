import pytest
import responses

from apprentice.helpers import action_ctx
from example.webhook import _fact_response, cool_fact_generator


@pytest.fixture(autouse=True)
def api_response(historical_fact_response):
    return responses.add(
        responses.GET,
        'https://history.muffinlabs.com/date',
        json=historical_fact_response,
        status=200)


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
                          'emeritus Diocletian confers with Galerius, '
                          'Augustus of the East, and Maximianus, the recently '
                          'returned former Augustus of the West, in an '
                          'attempt to end the civil wars of the Tetrarchy.',
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
