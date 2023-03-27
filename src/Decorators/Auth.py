from flask import request, session
from jwt import decode


def auth(func):
    def wrapper(*args, **kwargs):
        user_session = session.get("user")
        access_token = user_session['access_token']

        if (user_session is None):
            raise Exception("It's not possible to show this content for you.")

        result = decode(access_token, "secret", ["HS256"])
        print(result)

        func(*args, **kwargs)

    return wrapper
