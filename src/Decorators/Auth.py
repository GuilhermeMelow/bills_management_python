from flask import request, session
from os import environ as env
from requests import request as send_request
from jose import jwt

from src.Exceptions import AuthException


def get_jwt_token(raw: str):
    parts = raw.split()

    if not parts[0].lower() == "bearer":
        raise AuthException("Not contains bearer assigned")

    if parts.__len__() != 2:
        raise AuthException("Incorrect token format")

    return parts[1]


def get_rsa_key(token):
    jwks = send_request(
        url=f"https://{env.get('AUTH0_DOMAIN')}/.well-known/jwks.json",
        method="get").json()

    token_headers = jwt.get_unverified_header(token)
    key = next((jwk for jwk in jwks["keys"]
                if jwk["kid"] == token_headers["kid"]), None)

    return {
        "kty": key["kty"],
        "n": key["n"],
        "e": key["e"]
    }


def auth(func):
    def wrapper(*args, **kwargs):
        raw = request.headers.get("Authorization")
        token = get_jwt_token(raw)

        try:
            payload = jwt.decode(
                token,
                key=get_rsa_key(token),
                algorithms=env.get("AUTH0_ALGORITHMS"),
                audience=env.get("AUTH0_API_AUDIENCE"),
                issuer=f"https://{env.get('AUTH0_DOMAIN')}/")

            session["user_claims"] = payload

        except jwt.ExpiredSignatureError:
            raise AuthException("Token is expired.")

        except jwt.JWTClaimsError:
            raise AuthException("Incorrect claims, check aud and issuer.")

        except Exception:
            raise AuthException("Unable for authentication.")

        return func(*args, **kwargs)

    return wrapper
