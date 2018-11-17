import pytest


@pytest.fixture
def post_data():
    return {
        'originalRequest': {
            'source': 'google',
            'version': '2',
            'data': {
                'isInSandbox': True,
                'surface': {
                    'capabilities': [
                        {'name': 'actions.capability.AUDIO_OUTPUT'},
                        {'name': 'actions.capability.WEB_BROWSER'},
                        {'name': 'actions.capability.MEDIA_RESPONSE_AUDIO'},
                        {'name': 'actions.capability.SCREEN_OUTPUT'}
                    ]
                },
                'requestType': 'SIMULATOR', 'inputs': [{
                    'rawInputs': [{
                        'query': 'tell me a cool fact',
                        'inputType': 'KEYBOARD'}],
                    'arguments': [{
                        'rawText': 'tell me a cool fact',
                        'textValue': 'tell me a cool fact',
                        'name': 'text'
                    }],
                    'intent': 'actions.intent.TEXT'
                }],
                'user': {
                    'lastSeen': '2018-11-17T11:42:30Z',
                    'locale': 'en-US',
                    'userId': 'ABwppHG0IDYabNrx7x2UyAIxZ_MXZ0OvMjjDrVRV_FFBi7JTWSl0HdaJBVzBBgds26aheL3uWqjX4I5ZcffM6A'  # noqa
                },
                'conversation': {
                    'conversationId': 'ABwppHFiWZymymxHe12Z6BIRgwWAazMrwjE39vBgf1JgbHLNjeT_UUjb_VqqRAC7Rd73jBOJV34H8vsXjZLnjw',  # noqa
                    'type': 'ACTIVE',
                    'conversationToken': '[]'
                },
                'availableSurfaces': [{
                    'capabilities': [
                        {'name': 'actions.capability.AUDIO_OUTPUT'},
                        {'name': 'actions.capability.WEB_BROWSER'},
                        {'name': 'actions.capability.SCREEN_OUTPUT'}
                    ]
                }]
            }
        },
        'id': 'ee0059d0-d82c-4860-8395-707f1d8bca33',
        'timestamp': '2018-11-17T12:19:19.317Z', 'lang': 'en-us',
        'result': {
            'source': 'agent',
            'resolvedQuery': 'tell me a cool fact',
            'speech': '',
            'action': 'tell-fact',
            'actionIncomplete': False,
            'parameters': {
                'date': '',
                'History': ''
            },
            'contexts': [
                {
                    'name': 'actions_capability_screen_output',
                    'parameters': {
                        'date': '',
                        'History.original': '',
                        'date.original': '',
                        'History': ''
                    },
                    'lifespan': 0
                }, {
                    'name': 'actions_capability_audio_output',
                    'parameters': {
                        'date': '',
                        'History.original': '',
                        'date.original': '',
                        'History': ''
                    },
                    'lifespan': 0
                },
                {
                    'name': 'google_assistant_input_type_keyboard',
                    'parameters': {
                        'date': '',
                        'History.original': '',
                        'date.original': '',
                        'History': ''
                    },
                    'lifespan': 0
                }, {
                    'name': 'actions_capability_media_response_audio',
                    'parameters': {
                        'date': '',
                        'History.original': '',
                        'date.original': '',
                        'History': ''
                    },
                    'lifespan': 0
                }, {
                    'name': 'actions_capability_web_browser',
                    'parameters': {
                        'date': '',
                        'History.original': '',
                        'date.original': '',
                        'History': ''
                    },
                    'lifespan': 0
                }
            ],
            'metadata': {
                'isFallbackIntent': 'false',
                'intentName': 'tell-fact',
                'isResponseToSlotfilling': False,
                'intentId': 'af634b34-fe52-4e79-b321-c282493e6cfb',
                'webhookUsed': 'true',
                'webhookForSlotFillingUsed': 'true',
                'nluResponseTime': 94
            },
            'fulfillment': {
                'speech': '',
                'messages': []
            },
            'score': 1.0
        },
        'status': {'code': 200, 'errorType': 'success'},
        'sessionId': 'ABwppHFiWZymymxHe12Z6BIRgwWAazMrwjE39vBgf1JgbHLNjeT_UUjb_VqqRAC7Rd73jBOJV34H8vsXjZLnjw'  # noqa
    }
