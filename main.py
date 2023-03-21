from src.Controllers.Auth.AuthController import auth_controller
from src.Controllers.Bill.BillController import bill_controller

from os import environ as env
from dotenv import load_dotenv

from flask import Flask
from authlib.integrations.flask_client import OAuth


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = env.get("APP_SECRET_KEY")

    @app.get("/")
    def home():
        return "Everything is fine, there is no worries now :)"

    return app


if __name__ == "__main__":
    app = create_app()

    auth_controller(app)
    bill_controller(app)

    app.run(host="0.0.0.0", port=5002)
