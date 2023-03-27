from urllib.parse import quote_plus, urlencode
from flask import Flask, redirect, request, session, url_for
from authlib.integrations.flask_client import OAuth
from requests import PreparedRequest

from os import environ as env


def auth_controller(app: Flask):
    oauth = OAuth(app)
    oauth.register(
        name="bills_management",
        overwrite=True,
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
    )

    @app.get("/login")
    def login():
        args = request.args

        req = PreparedRequest()
        req.prepare_url(url=url_for("callback", _external=True),
                        params={'uri': args.get('callback')})

        return oauth.bills_management.authorize_redirect(redirect_uri=req.url)

    @ app.get("/callback")
    def callback():
        args = request.args

        token = oauth.bills_management.authorize_access_token()
        session["user"] = token

        return redirect(args.get('uri'))

    @ app.get("/logout")
    def logout():
        session.clear()

        encode = urlencode({
            "returnTo": url_for("home", _external=True),
            "client_id": env.get("AUTH0_CLIENT_ID"),
        }, quote_via=quote_plus)

        return redirect(f'https://{env.get("AUTH0_DOMAIN")}/v2/logout?{encode}')
