from os import environ as env
from dotenv import load_dotenv
from flask import Flask, make_response
from src.Controllers.Bill.BillController import bill_controller

from src.Exceptions import ApiException

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = env.get("APP_SECRET_KEY")

    @app.get("/")
    def home():
        return "Everything is fine, there is no worries now :)"

    @app.errorhandler(ApiException)
    def auth_error_handler(exception: ApiException):
        return make_response(exception.__dict__, exception.code)

    with app.app_context():
        bill_controller()

    app.run(host="0.0.0.0", port=5002)


if __name__ == "__main__":
    create_app()
