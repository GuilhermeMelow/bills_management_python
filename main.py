from flask import Flask

from src.Controllers.Bill.BillController import bill_controller


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def testing_default():
        return "Everything is fine, there is no worries now :)"

    return app


if __name__ == "__main__":
    app = create_app()

    bill_controller(app)

    app.run(host="0.0.0.0")
