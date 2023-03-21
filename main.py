from src.Controllers.Bill.BillController import bill_controller

from os import environ as env
from dotenv import load_dotenv
from urllib.parse import quote_plus, urlencode

from flask import Flask, redirect, session, url_for
from authlib.integrations.flask_client import OAuth


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = env.get("APP_SECRET_KEY")

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
        return oauth.bills_management.authorize_redirect(
            redirect_uri=url_for("callback", _external=True),
        )

    @app.get("/callback")
    def callback():
        token = oauth.bills_management.authorize_access_token()
        session["user"] = token

        return redirect("/")

    @app.get("/logout")
    def logout():
        session.clear()

        encode = urlencode({
            "returnTo": url_for("home", _external=True),
            "client_id": env.get("AUTH0_CLIENT_ID"),
        }, quote_via=quote_plus)

        return redirect(f'https://{env.get("AUTH0_DOMAIN")}/v2/logout?{encode}')

    @app.get("/")
    def home():
        return "Everything is fine, there is no worries now :)"

    return app


if __name__ == "__main__":
    app = create_app()

    bill_controller(app)

    app.run(host="0.0.0.0", port=5002)
