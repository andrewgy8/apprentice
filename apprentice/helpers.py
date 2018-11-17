from flask import Flask


def action_ctx_test(function):
    def wrap_function(*args, **kwargs):
        flask_app = Flask(__name__)
        with flask_app.test_request_context():
            return function(*args, **kwargs)
    return wrap_function
